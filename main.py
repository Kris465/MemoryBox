import asyncio
import os
from dotenv import load_dotenv, find_dotenv
from loguru import logger
from aiogram import Bot, Dispatcher

from channel import channel_router
from private_chat import private_router
from group_chat import group_router


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

    dp.include_router(private_router)
    dp.include_router(group_router)
    dp.include_router(channel_router)

    logger.info("Бот запущен")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
