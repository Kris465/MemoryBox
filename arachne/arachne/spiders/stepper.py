import json
from urllib.parse import urljoin, urlparse
import scrapy
from ..items import ChapterItem


class Stepper(scrapy.Spider):
    name = "stepper"

    def __init__(self, site_key=None, start_url=None,
                 chapter_num=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.current_chapter = int(chapter_num)
        self.site_key = site_key

        self.config = self.load_config(site_key)
        if not self.config:
            raise ValueError(f"No config found for {site_key}")

    def load_config(self, site_key):
        """Теперь загружает по site_key вместо URL"""
        with open("configs/stepper_config.json") as f:
            configs = json.load(f)
        return configs.get("sites", {}).get(site_key)

    def parse(self, response):
        item = ChapterItem(
            url=response.url,
            chapter_number=self.current_chapter,
            content=response.css(self.config["content_selector"]).get(),
            domain=urlparse(response.url).netloc
        )
        yield item

        next_page = response.css(self.config["next_selector"]).get()
        if next_page:
            self.current_chapter += 1
            if not next_page.startswith(('http://', 'https://')):
                next_page = urljoin(self.config["base_url"], next_page)
            yield response.follow(next_page, callback=self.parse)
