import scrapy
import json
from urllib.parse import urlparse


class NovelCheckerSpider(scrapy.Spider):
    name = "novel_checker"

    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url] if url else []
        self.selectors = self.load_selectors()

    def load_selectors(self):
        with open("selectors.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def get_domain(self, url):
        return urlparse(url).netloc

    def parse(self, response):
        domain = self.get_domain(response.url)
        selectors = self.selectors.get(domain, {})

        next_chapter = response.css(selectors["next_chapter"]).get() if "next_chapter" in selectors else None
        yield {"is_updated": bool(next_chapter)}
