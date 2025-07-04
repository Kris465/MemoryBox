import asyncio
from twisted.internet import asyncioreactor
asyncioreactor.install()
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from ..utils.file_loader import load_novels


class SpiderManager:
    def __init__(self):
        configure_logging()
        self.runner = CrawlerRunner(get_project_settings())
        self.active_tasks = {}
        
    async def run_spider(self, url):
        """Запуск одного паука"""
        deferred = self.runner.crawl("novel_checker", url=url)
        result = await deferred
        return result.get("is_updated", False)

    async def check_all_novels(self):
        """Проверка всех новелл"""
        novels = load_novels()
        results = {}

        for title, url in novels.items():
            is_updated = await self.run_spider(url)
            results[title] = {
                "url": url,
                "is_updated": is_updated
            }

        return results

    async def periodic_check(self, interval=3600):
        """Периодическая проверка"""
        while True:
            results = await self.check_all_novels()
            yield results
            await asyncio.sleep(interval)
