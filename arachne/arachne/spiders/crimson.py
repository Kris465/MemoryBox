import scrapy
from loguru import logger


class CrimsonSpider(scrapy.Spider):
    name = "crimson"
    start_urls = [
        "https://www.crimsontranslations.com/51-a-silly-little-snakes-mishap/419"
    ]

    def parse(self, response):
        logger.info(f"Processing page: {response.url}")

        chapter_content = response.css('.entry-content').get()
        next_page = response.css('.nav-next a::attr(href)').get()

        yield {
            'url': response.url,
            'content': chapter_content,
        }

        if next_page:
            yield response.follow(next_page, callback=self.parse)
