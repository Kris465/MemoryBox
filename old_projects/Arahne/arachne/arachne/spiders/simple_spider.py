import scrapy
from scrapy.http import Request


class SimpleSpider(scrapy.Spider):
    name = "simple_spider"
    start_urls = ["https://www.gismeteo.ru/weather-korolev-11404/"]

    # Асинхронный метод (Scrapy 2.13+)
    async def start(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, errback=self.handle_error)

    # Обработка успешного ответа
    async def parse(self, response):
        self.logger.info(f"Processing: {response.url}")
        
        # Пример извлечения данных
        yield {
            "url": response.url,
            "title": response.css("title::text").get(),
            "status": response.status,
        }

        # Пример добавления новых ссылок (если нужно)
        # for link in response.css("a::attr(href)").getall():
        #     yield response.follow(link, callback=self.parse)

    # Обработка ошибок
    async def handle_error(self, failure):
        self.logger.error(f"Failed to process: {failure.request.url}. Error: {failure.value}")