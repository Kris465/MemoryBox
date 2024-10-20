import random
from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from bs4 import BeautifulSoup
import requests

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помощник')


@user_private_router.message(or_f(Command("joke"),
                                  (F.text.lower().contains("анекдот"))))
async def tell_private_joke(message: types.Message):
    response = requests.get('https://www.anekdot.ru/random/anekdot/')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        jokes = soup.find_all('div', class_='text')
        random_joke = random.choice(jokes).text.strip()
        anekdot = random_joke
    else:
        anekdot = "Не удалось найти анекдот"

    await message.answer(anekdot)
