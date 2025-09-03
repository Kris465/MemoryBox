import asyncio
import os

from aiogram import Bot, Dispatcher
from loguru import logger
from dotenv import load_dotenv, find_dotenv

from checker import Checker
from tools.file_manager import read_from_json, update_novels_file

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def process_novel(title, link):
    """Обработка одной новелы"""
    logger.info(f"{title}: {link}")

    checker = Checker(link)
    await checker.logic()
    if checker.result:
        await bot.send_message(chat_id=CHANNEL_ID,
                               text=f'{title}: {checker.link}.',
                               parse_mode='HTML')
        update_novels_file(title, checker.link)


async def main_logic():
    while True:
        links = read_from_json('novels.json')
        tasks = []
        for title, link in links.items():
            task = asyncio.create_task(process_novel(title, link))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

        await asyncio.sleep(5)


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)

    logger.info("Запуск бота")
    main_task = asyncio.create_task(main_logic())
    await dp.start_polling(bot)
    main_task.cancel()
    try:
        await main_task
    except asyncio.CancelledError:
        pass


if __name__ == '__main__':
    asyncio.run(main())
