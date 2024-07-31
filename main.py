import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение токена из переменных окружения
API_TOKEN = os.getenv('API_TOKEN')


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def send_welcome(message: types.Message):
        await message.answer("Привет! Я бот-анекдотист. Напиши /anekdot, чтобы получить анекдот.")

    @dp.message(Command("anekdot"))
    async def send_anekdot(message: types.Message):
        response = requests.get('https://www.anekdot.ru/random/anekdot/')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            jokes = soup.find_all('div', class_='text')

            random_joke = random.choice(jokes).text.strip()
            anekdot = random_joke
        else:
            anekdot = "Не удалось получить анекдот"
        await message.answer(anekdot)

    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
