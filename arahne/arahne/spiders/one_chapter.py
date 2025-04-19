import scrapy


class OneChapterSpider(scrapy.Spider):
    name = "one_chapter"
    allowed_domains = ["translatingboredom.com"]
    start_urls = ["https://translatingboredom.com/2021/03/27/ttbe-1/"]

    def parse(self, response):
        pass
