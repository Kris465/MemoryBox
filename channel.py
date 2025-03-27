import asyncio
import os
from random import choice
from dotenv import find_dotenv, load_dotenv
from aiogram import Router, types, Bot
from aiogram import Command
import requests
from loguru import logger
from bs4 import BeautifulSoup


load_dotenv(find_dotenv())
CHANNEL_ID = os.getenv("CHANNEL_ID")

channel_router = Router()


async def send_random_joke(bot: Bot):
    while True:
        try:
            response = requests.get("https://www.anekdot.ru/random/anekdot/")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                jokes = soup.find_all('div', class_='text')
                random_joke = choice(jokes).text.stip()
                anekdot = random_joke
            else:
                anekdot = "Не удалось получить анекдот"
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения {e}")

        await asyncio.sleep(30)


@channel_router.message(Command('start'))
async def channel_start(message: types.Message):
    await message.answer("Этот бот работает в канале и отправляет анекдоты!")
