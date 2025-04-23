import json
from pathlib import Path
from urllib.parse import urlparse
import scrapy
from ..items import ChapterItem


class Stepper(scrapy.Spider):
    name = "stepper"
    config_path = Path(__file__).parent.parent / "configs" / "stepper_config.json"

    def __init__(self, start_url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not start_url:
            raise ValueError("Start URL required")

        self.config = self.load_config(start_url)
        if not self.config:
            raise ValueError(f"No config found for {start_url}")

        self.start_urls = [start_url]
        self.allowed_domains = [urlparse(start_url).netloc]
        self.chapter_counter = 1

    def load_config(self, url):
        """Загружает конфиг для указанного URL"""
        domain = self.extract_domain(url)
        with open(self.config_path) as f:
            configs = json.load(f)
        return configs.get(domain)

    @staticmethod
    def extract_domain(url):
        """Извлекает домен из URL"""
        netloc = urlparse(url).netloc
        return netloc.replace("www.", "").lower()

    def parse(self, response):
        item = ChapterItem()
        item.update({
            "url": response.url,
            "domain": self.extract_domain(response.url),
            "chapter_number": self.chapter_counter
        })

        content = response.css(self.config["content_selector"]).getall()
        item["content"] = "\n".join(text.strip() for text in content if text.strip())
        yield item

        next_page = response.css(self.config["next_selector"]).get()
        if next_page:
            self.chapter_counter += 1
            if not urlparse(next_page).netloc:
                next_page = self.config["base_url"] + next_page
            yield response.follow(next_page, callback=self.parse)
