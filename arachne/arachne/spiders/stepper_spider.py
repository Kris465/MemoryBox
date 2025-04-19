# spiders/stepper_spider.py
from .base_spider import BaseSpider

class StepperSpider(BaseSpider):
    name = "stepper_spider"
    
    def __init__(self, url=None, title=None, start_chapter=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]
        self.title = title
        self.current_chapter = start_chapter
        self.config = self.load_config("stepper", url)

    def parse(self, response):
        # Парсинг контента
        text = response.css(self.config["content_selector"] + "::text").getall()
        self.save_chapter(text)

        # Проверка условий остановки
        if any(stop_word in response.text for stop_word in self.config.get("stop_conditions", [])):
            logger.info(f"Stop condition met at chapter {self.current_chapter}")
            return

        # Переход к следующей главе
        next_page = response.css(self.config["next_selector"]).attrib.get("href")
        if next_page:
            yield response.follow(next_page, callback=self.parse)