# Бот - анекдот

Задача 1: Создайте новый проект в PyCharm. 

Задача 2: Установите библиотеки: requests (для запросов к интернет-ресурсам), beautifulsoup4 (чтобы распарсить полученный от сервера html код), aiogram (для доступа к API телеграма). 

* pip install aiogram==2.25.1

* pip install beautifulsoup4

* pip install requests

Задача 3: Напишите код бота:

```python
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
    await message.reply("Привет! Я бот-анекдотист. Напиши /anekdot, чтобы получить анекдот.")


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
```

Задача 4: Если уже есть волшебный ключик, используйте его в коде. Если же нет, то: зайдите в телеграм и найдите отца всех ботов телеграма: @BotFather (он должен быть с синей галочкой). Введите команду: /newbot. Теперь придумайте общее название для бота. Далее придумайте конкретное название, которое заканчивается на “bot”. В ответном сообщении вы получите ключ (набор символов и букв) для управления ботом. Возьмите ключ и вставьте его в строчку с ключом.

Задача 5: Создайте файл со списком всех использованных в проекте библиотек с помощью команды: pip freeze > requirements.txt. Откройте файл и посмотрите, отличается количество библиотек от тех, что мы установили или нет.

Задача 6: Запустите бота и протестируйте его работу.
