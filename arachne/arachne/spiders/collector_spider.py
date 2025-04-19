# spiders/collector_spider.py
from .base_spider import BaseSpider


class CollectorSpider(BaseSpider):
    name = "collector_spider"

    def __init__(self, toc_url=None, title=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [toc_url]
        self.title = title
        self.config = self.load_config("collector", toc_url)

    def parse(self, response):
        toc = response.css(self.config["toc_selector"])
        chapter_links = toc.css(self.config["chapter_links"] + "::attr(href)").getall()

        for link in chapter_links:
            yield response.follow(link, callback=self.parse_chapter)

    def parse_chapter(self, response):
        text = response.css(self.config["content_selector"] + "::text").getall()
        self.save_chapter(text)
