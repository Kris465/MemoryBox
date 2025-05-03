import json
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ..spiders.stepper import Stepper
from loguru import logger
from twisted.internet import reactor


logger.add(
    "file.log",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    rotation="3 days",
    backtrace=True,
    diagnose=True
)


class SpiderCLI:
    def __init__(self, spider_name: str = "stepper"):
        self.spider_name = spider_name.lower()
        self.config_dir = Path(__file__).parent.parent / "configs"
        self.config_file = self.config_dir / f"{self.spider_name}_config.json"
        self.raw_config = self._load_config()
        logger.info(f"CLI initialized for {self.spider_name}")

    def load_config(self, site_key: Optional[str]) -> Optional[Dict[str, Any]]:
        """Загружает конфиг для указанного сайта"""
        if not site_key:
            return None

        config_path = Path(__file__).parent.parent / "configs" / "stepper_config.json"

        logger.debug(f"Looking for config at: {config_path.absolute()}")

        if not config_path.exists():
            logger.error(f"Config file not found at {config_path.absolute()}")
            return None

        try:
            with open(config_path, "r", encoding="utf-8") as f:
                configs = json.load(f)
                logger.debug(f"Config content: {json.dumps(configs, indent=2)}")
                return configs.get(site_key)
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return None

    def run(self) -> None:
        """Основной цикл приложения"""
        logger.info("Starting Arachne CLI")
        try:
            while True:
                print("\nOptions:")
                print("1. Parse novel")
                print("2. List available sites")
                print("3. Exit")

                choice = input("Select option: ").strip()
                logger.debug(f"User selected: {choice}")

                if choice == "1":
                    self._handle_parse()
                elif choice == "2":
                    self._list_sites()
                elif choice == "3":
                    logger.info("Exiting application")
                    break
                else:
                    print("Invalid option, try again")
        except KeyboardInterrupt:
            logger.info("Received exit signal, shutting down")
        finally:
            if reactor.running:
                reactor.stop()

    def _handle_parse(self) -> None:
        """Обработка парсинга новеллы"""
        url = input("Enter starting chapter URL: ").strip()
        if not url:
            logger.warning("Empty URL provided")
            return

        site_config = self._get_site_config(url)
        if not site_config:
            logger.warning(f"No config found for URL: {url}")
            print("No matching site configuration found")
            return

        chapter_num = input("Enter chapter number (default: 1): ").strip()
        chapter_num = int(chapter_num) if chapter_num.isdigit() else 1
        output_file = input("Output filename (default: output.json): "
                            ).strip() or "output.json"

        self._run_spider(
            config=site_config,
            start_url=url,
            output_file=output_file,
            chapter_num=chapter_num
        )

    def _get_site_config(self, url: str) -> Optional[Dict[str, Any]]:
        """Возвращает конфиг для указанного URL"""
        domain = self._extract_domain(url)
        if not domain:
            return None

        for site_name, site_config in self.raw_config.items():
            config_domain = self._extract_domain(site_config.get('base_url',
                                                                 ''))
            if domain == config_domain:
                logger.debug(f"Matched config: {site_name} for {url}")
                return site_config

        return None

    def _extract_domain(self, url: str) -> Optional[str]:
        """Извлекает домен из URL"""
        if not url:
            return None

        parsed = urlparse(url)
        if not parsed.netloc:
            return None

        domain = parsed.netloc.replace("www.", "").split(':')[0]
        return domain.split('.')[0]

    def _list_sites(self) -> None:
        """Выводит список доступных сайтов"""
        if not self.raw_config:
            print("No site configurations available")
            return

        print("\nAvailable sites:")
        for i, (site_name, config) in enumerate(self.raw_config.items(), 1):
            base_url = config.get('base_url', 'N/A')
            print(f"{i}. {site_name} ({base_url})")

    def _run_spider(self, config: Dict[str, Any], start_url: str,
                    output_file: str, chapter_num: int = 1) -> None:
        """Запускает паука с указанными параметрами"""
        logger.info(f"Starting spider with config: {config}")

        novels_dir = Path("novels")
        novels_dir.mkdir(exist_ok=True)

        output_path = novels_dir / output_file

        settings = get_project_settings()
        settings.update({
            "FEEDS": {
                str(output_path): {
                    "format": "json",
                    "encoding": "utf8",
                    "indent": 2,
                    "overwrite": True,
                },
            },
            "LOG_LEVEL": "INFO",
            "DOWNLOAD_HANDLERS": {
                "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
                "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            },
            "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
            "PLAYWRIGHT_BROWSER_TYPE": "chromium",
        })

        try:
            process = CrawlerProcess(settings)
            process.crawl(
                Stepper,
                site_key=self._extract_domain(start_url),
                start_url=start_url,
                chapter_num=chapter_num
            )
            process.start()
            logger.success(f"Spider completed successfully. Results saved to {output_path}")
        except Exception as e:
            logger.error(f"Spider failed: {e}")
            raise


if __name__ == "__main__":
    cli = SpiderCLI()
    cli.run()
