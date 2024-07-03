import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from bs4 import BeautifulSoup
import requests

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Я бот-анекдотист. Напиши /anekdot, чтобы получить анекдот.")


@dp.message_handler(commands=['anekdot'])
async def send_anekdot(message: types.Message):
    response = requests.get('https://www.anekdot.ru/random/anekdot/')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        jokes = soup.find_all('div', class_='text')

        random_joke = random.choice(jokes).text.strip()
        anekdot = random_joke
    else:
        anekdot = "Не удалось получить анекдот"
    await message.reply(anekdot)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())
    loop.run_forever()
