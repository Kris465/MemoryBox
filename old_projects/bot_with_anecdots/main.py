import os

from random import choice
import requests
import asyncio
from loguru import logger
from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from database import Database


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
dp = Dispatcher()
database = Database()


@dp.message(Command("start"))
async def command_start_handler(message: Message):
    database.create_user([message.from_user.id,
                          message.from_user.first_name,
                          message.from_user.last_name,
                          message.from_user.username,
                          message.from_user.language_code])
    await message.answer("Привет! Я рассказываю анекдоты!\nИспользуй:\n/start\n/anekdot")


@dp.message(Command("anekdot"))
async def send_anekdot(message: Message):
    response = requests.get('http://www.anekdot.ru/random/anekdot/')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        jokes = soup.find_all('div', class_='text')

        random_joke = choice(jokes).text.strip()
        anekdot = random_joke
    else:
        anekdot = "Не удалось получить анекдот"

    await message.answer(anekdot)


async def main():
    logger.add('file.log',
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days")

    bot = Bot(token=TOKEN)
    logger.info("Бот создан... ")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
