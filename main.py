import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from loguru import logger
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)

    logger.info("Запуск бота")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
