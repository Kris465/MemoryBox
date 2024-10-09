import random
from aiogram import F, types, Router
from aiogram.filters import Command
from bs4 import BeautifulSoup
import requests

general_router = Router()


@general_router.message(F.text.contains("анекдот"))
@general_router.message(Command("joke"))
async def tell_joke(message: types.Message):
    response = requests.get('https://www.anekdot.ru/random/anekdot/')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        jokes = soup.find_all('div', class_='text')
        random_joke = random.choice(jokes).text.strip()
        anekdot = random_joke
    else:
        anekdot = "Не удалось найти анекдот"

    await message.answer(anekdot)
