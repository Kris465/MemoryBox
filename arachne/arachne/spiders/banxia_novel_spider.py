import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy import signals


class BanxiaNovelSpider(scrapy.Spider):
    name = 'banxia_novel'
    result = {}

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS': 1,
        'RETRY_TIMES': 2,
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chapters_toc = self.load_chapters_toc()

    def load_chapters_toc(self):
        try:
            with open('chapters_toc.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            self.logger.error("❌ Файл chapters_toc.json не найден!")
            return {}

    def start_requests(self):
        if not self.chapters_toc:
            return

        for chapter_id, chapter_data in self.chapters_toc.items():
            yield scrapy.Request(
                chapter_data['url'],
                meta={'chapter_id': chapter_id},
                callback=self.parse_chapter,
                errback=self.handle_error
            )

    def parse_chapter(self, response):
        chapter_id = response.meta['chapter_id']

        text = "\n".join(
            response.css('#nr1 ::text').getall() or 
            response.css('.chapter-content ::text').getall()
        ).strip()

        self.result[chapter_id] = f"{response.url}\n\n{text}"

        self.logger.info(f"✅ Глава {chapter_id} обработана")

    def handle_error(self, failure):
        chapter_id = failure.request.meta['chapter_id']
        error_msg = f"🚫 Ошибка в главе {chapter_id}: {str(failure.value)}"
        self.result[chapter_id] = f"{failure.request.url}\n\n{error_msg}"
        self.logger.error(error_msg)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.save_result, signal=signals.spider_closed)
        return spider

    def save_result(self, spider, reason):
        """Сохранение при любом завершении"""
        with open('novel_full.json', 'w', encoding='utf-8') as f:
            json.dump(self.result, f, ensure_ascii=False, indent=2)

        stats = (
            f"📊 Итог:\n"
            f"Всего глав: {len(self.chapters_toc)}\n"
            f"Успешно: {sum(1 for v in self.result.values() if '🚫' not in v)}\n"
            f"Ошибки: {sum(1 for v in self.result.values() if '🚫' in v)}"
        )
        self.logger.info(stats)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(BanxiaNovelSpider)
    process.start()
