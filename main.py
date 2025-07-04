import asyncio
from loguru import logger
from novel_checker.core.spider_manager import SpiderManager


async def main():
    manager = SpiderManager()

    async for results in manager.periodic_check(interval=100):
        for title, data in results.items():
            if data["is_updated"]:
                logger.info(f"Обновление в '{title}': {data['url']}")


if __name__ == "__main__":
    asyncio.run(main())
