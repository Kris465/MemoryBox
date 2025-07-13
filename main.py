import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from loguru import logger
from dotenv import load_dotenv, find_dotenv

from handlers import cmd_start, process_name, process_age, Form

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

    dp.message.register(cmd_start, Command('start'))
    dp.message.register(process_name, Form.name)
    dp.message.register(process_age, Form.age)

    logger.info("Запуск бота")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
