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


async def main_logic():
    while True:
        links = read_from_json('novels.json')

        for title, link in links.items():
            logger.info(f"{title}: {link}")

            checker = Checker(link)
            checker.logic()
            if checker.result:
                await bot.send_message(chat_id=CHANNEL_ID,
                                       text=f'{title}: {checker.link}.',
                                       parse_mode='HTML')
                update_novels_file(title, checker.link)
        await asyncio.sleep(5)


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)

    logger.info("Запуск бота")

    await main_logic()

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
