import os
import asyncio
from loguru import logger
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days", backtrace=True, diagnose=True)

    bot = Bot(TOKEN)
    logger.info("Бот создан")
    dp = Dispatcher()
    logger.info("Диспетчер создан")

    @dp.message(Command('start'))
    async def send_welcome(message: types.Message):
        await message.answer("Привет, Я эхо-бот!")
        await message.answer("Мои команды: /start и /help")
        logger.info("Бот ответил на команду /start")

    @dp.message(Command("help"))
    async def help(message: types.Message):
        await message.answer("Ты можешь отправить мне сообщение, я верну его тебе")
        logger.info("Бот объяснил, что делает")

    @dp.message()
    async def echo(message: types.Message):
        await message.answer(message.text)
        logger.info(f"Бот вернул пользователю сообщение {message.text}")

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
