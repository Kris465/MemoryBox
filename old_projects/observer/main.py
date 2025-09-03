import hashlib
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from loguru import logger

from aiogram import Bot, Dispatcher

from bot.handlers import setup_handlers
from bot.observer import NewsSubject
from bot.services import get_news


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    news_subject = NewsSubject()

    setup_handlers(dp, news_subject, bot)

    task = asyncio.create_task(check_news_periodically())

    logger.info("Бот запущен")

    try:
        await dp.start_polling(bot)
    finally:
        task.cancel()
        await bot.session.close()
        logger.info("Бот остановлен")


async def check_news_periodically():
    last_hash = None
    while True:
        new_news = get_news(limit=5)
        current_hash = hash_news(new_news)

        if current_hash != last_hash:
            logger.info(f"Обнаружены новые новости: {len(new_news)} шт.")
            await news_subject.notify(new_news)
            last_hash = current_hash
        else:
            logger.debug("Нет новых новостей")

        await asyncio.sleep(20)


def hash_news(news_list):
    combined = ''.join(item['title'] for item in news_list)
    return hashlib.sha256(combined.encode()).hexdigest()


if __name__ == '__main__':
    asyncio.run(main())
