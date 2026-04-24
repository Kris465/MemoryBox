import os
from random import choice
import asyncio
from bs4 import BeautifulSoup
from loguru import logger
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import find_dotenv, load_dotenv
import requests


load_dotenv(find_dotenv())
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days", backtrace=True, diagnose=True)

    bot = Bot(TOKEN)
    logger.info("Бот создан")
    dp = Dispatcher()
    logger.info("Диспетчер создан")

    async def send_anekdot():
        while True:
            try:
                response = requests.get('https://www.anekdot.ru/random/anekdot/')
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    jokes = soup.find_all('div', class_='text')

                    random_joke = choice(jokes).text.strip()
                    anekdot = random_joke

                await bot.send_message(CHANNEL_ID, anekdot)
                logger.info({anekdot})
            except Exception as e:
                logger.error(f"Ошибка при отправке сообщения: {e}")
            await asyncio.sleep(30)

    @dp.message(Command("start"))
    async def start_command(message: types.Message):
        await message.answer(
            "Бот запущен! Случайные числа будут отправляться в канал.")

    task = asyncio.create_task(send_anekdot())

    try:
        await dp.start_polling(bot)
    finally:
        task.cancel()
        await bot.session.close()
        logger.info("Бот остановлен")


if __name__ == '__main__':
    asyncio.run(main())
