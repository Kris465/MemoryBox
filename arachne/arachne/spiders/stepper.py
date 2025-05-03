import json
from pathlib import Path
from urllib.parse import urljoin, urlparse
from typing import Dict, Any, Optional, Union, Iterator
from loguru import logger

import scrapy
from scrapy_playwright.page import PageMethod
from ..items import ChapterItem


class Stepper(scrapy.Spider):
    name = "stepper"
    custom_settings = {
        'LOG_LEVEL': 'ERROR',
        'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor',
    }

    def __init__(
        self,
        site_key: Optional[str] = None,
        start_url: Optional[str] = None,
        chapter_num: int = 1,
        *args: Any,
        **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)
        if not start_url:
            logger.error("No start URL provided")
            raise ValueError("Start URL is required")

        self.start_urls = [start_url]
        self.current_chapter = int(chapter_num)
        self.site_key = site_key or self._extract_domain(start_url)
        self.config = self.load_config(self.site_key)

        logger.info(f"Starting spider for {start_url}")
        logger.info(f"Initial chapter: {self.current_chapter}")
        logger.debug(f"Loaded config: {self.config}")

        if not self.config:
            logger.error(f"No config found for {self.site_key}")
            raise ValueError(f"No config found for {self.site_key}")

        self.config.setdefault("base_url", start_url)

    def _extract_domain(self, url: str) -> str:
        """Извлекает домен из URL для использования как site_key"""
        parsed = urlparse(url)
        return parsed.netloc.replace("www.", "").split(':')[0]

    def load_config(self, site_key: Optional[str]) -> Optional[Dict[str, Any]]:
        """Загружает конфиг для указанного сайта"""
        if not site_key:
            return None

        config_path = Path(__file__).parent.parent / "configs" / "stepper_config.json"
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                configs = json.load(f)
                logger.debug(f"Loaded config file for {site_key}")
                return configs.get(site_key)
        except FileNotFoundError:
            logger.error(f"Config file not found at {config_path}")
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config: {e}")
        except Exception as e:
            logger.error(f"Unexpected error loading config: {e}")
        return None

    def start_requests(self):
        for url in self.start_urls:
            logger.info(f"Initiating request with Playwright: {url}")
            yield scrapy.Request(
                url,
                meta={
                    "playwright": True,
                    "playwright_page_methods": [
                        PageMethod("wait_for_selector",
                                   self.config["content_selector"],
                                   timeout=10000),
                        PageMethod("screenshot", path="debug.png",
                                   full_page=True)
                    ],
                    "playwright_context_kwargs": {
                        "java_script_enabled": True,
                        "ignore_https_errors": True,
                        "viewport": {"width": 1920, "height": 1080}
                    }
                },
                callback=self.parse,
                errback=self.errback
            )

    def parse(self, response: scrapy.http.Response) -> Iterator[Union[ChapterItem, scrapy.Request]]:
        """Обрабатывает страницу главы"""
        logger.info(f"Processing chapter {self.current_chapter} | {response.url}")

        content = response.css(self.config["content_selector"]).get()
        if not content:
            logger.warning(f"No content found using selector: {self.config['content_selector']}")

        logger.debug(f"Content length: {len(content or '')} chars")

        yield ChapterItem(
            url=response.url,
            chapter_number=self.current_chapter,
            content=content,
            domain=urlparse(response.url).netloc
        )

        next_page = response.css(self.config["next_selector"]).get()
        if next_page:
            self.current_chapter += 1
            if not next_page.startswith(('http://', 'https://')):
                next_page = urljoin(self.config["base_url"], next_page)

            logger.info(f"Found next chapter link: {next_page}")
            yield response.follow(
                next_page,
                callback=self.parse,
                meta={
                    "playwright": True,
                    "playwright_page_methods": [
                        PageMethod(
                            "wait_for_selector",
                            self.config["content_selector"],
                            timeout=10000
                        ),
                    ],
                },
                errback=self.errback
            )
        else:
            logger.success(f"Finished parsing. Total chapters: {self.current_chapter - 1}")

    async def errback(self, failure):
        """Обработка ошибок"""
        page = failure.request.meta.get("playwright_page")
        if page:
            await page.close()

        logger.error(f"Failed to process chapter {self.current_chapter}")
        logger.error(f"URL: {failure.request.url}")
        logger.error(f"Error: {failure.value}")

        # Можно добавить повторную попытку
        if hasattr(failure.request, 'retries'):
            retries = failure.request.retries
            if retries < 3:
                logger.warning(f"Retrying ({retries + 1}/3)...")
                failure.request.retries = retries + 1
                yield failure.request
