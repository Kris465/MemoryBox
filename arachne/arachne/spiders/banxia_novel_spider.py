import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_playwright.page import PageCoroutine
import json


class BanxiaNovelSpider(scrapy.Spider):
    name = 'banxia_novel'

    def start_requests(self):
        url = "https://www.banxia.la/books/337775.html"
        yield scrapy.Request(
            url,
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "playwright_page_coroutines": [
                    PageCoroutine("wait_for_selector", "div.chapter-list"),
                ],
            },
            callback=self.parse_toc
        )

    async def parse_toc(self, response):
        chapters = {}
        for idx, link in enumerate(response.css('div.chapter-list a'), start=1):
            chapter_url = response.urljoin(link.attrib['href'])
            chapter_title = link.css('::text').get().strip()
            chapters[str(idx)] = {
                "url": chapter_url,
                "title": chapter_title
            }

        self.logger.info("\n\nСобраны ссылки на главы:")
        for num, data in chapters.items():
            self.logger.info(f"{num}. {data['title']} - {data['url']}")
        with open("chapters.json", "w", encoding="utf-8") as f:
            json.dump(chapters, f, ensure_ascii=False, indent=2)
        return chapters


if __name__ == "__main__":
    process = CrawlerProcess(settings={
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "PLAYWRIGHT_BROWSER_TYPE": "chromium",
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "FEEDS": {
            "chapters.json": {
                "format": "json",
                "encoding": "utf8",
                "overwrite": True
            }
        }
    })

    process.crawl(BanxiaNovelSpider)
    process.start()