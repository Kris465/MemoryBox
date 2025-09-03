import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.methods import DeleteWebhook
from aiogram.types import Message

from pydantic import BaseModel
from mistralai import Mistral
from instructor import from_mistral, Mode
import requests


TOKEN = '' # ВСТАВЬТЕ ТОКЕН БОТА⁡
client = Mistral(api_key="") # ЗАМЕНИТЕ АПИ КЛЮЧ НА ВАШ https://console.mistral.ai/api-keys
instructor_client = from_mistral(client=client, mode=Mode.MISTRAL_TOOLS)

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher()


# КЛАСС ДЛЯ СТРУКТУРИРОВАННОГО ВЫВОДА
class WeatherInfo(BaseModel):
    city: str


# ФУНКЦИЯ ПОЛУЧЕНИЯ ПОГОДЫ
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"  # JSON format
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        current = data['current_condition'][0]
        weather = {
            'temperature_C': current['temp_C'],
            'feels_like_C': current['FeelsLikeC'],
            'description': current['weatherDesc'][0]['value'],
            'humidity': current['humidity'],
            'wind_kph': current['windspeedKmph']
        }
        return weather
    else:
        return {"error": f"Could not retrieve weather data: {response.status_code}"}


# ⁡⁢⁣⁡⁢⁣⁣ОБРАБОТЧИК КОМАНДЫ СТАРТ⁡⁡
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('Привет! Я - бесплатный ИИ Агент, который может рассказать, какая сейчас погода.')


# ⁡⁢⁣⁣ОБРАБОТЧИК ЛЮБОГО ТЕКСТОВОГО СООБЩЕНИЯ⁡
@dp.message(F.text)
async def filter_messages(message: Message):
    # СОЗДАНИЕ ПРОМПТА
    user_prompt = message.text

    # ПОЛУЧЕНИЕ СТРУКТУРИРОВАННОГО ОТВЕТА
    ai_response = instructor_client.chat.completions.create(
        response_model=WeatherInfo,
        model="mistral-large-latest",
        messages=[{"role": "user", "content": user_prompt}],
        temperature=0,
    )

    # ВЫВОД ОТВЕТА
    print(ai_response)

    # ВЫЗОВ ФУНКЦИИ ПОЛУЧЕНИЯ ПОГОДЫ
    weather_info = get_weather(ai_response.city)
    print(weather_info)

    # ВТОРОЙ ЗАПРОС В ИИ С РЕЗУЛЬТАТАМИ О ГОРОДЕ И ПОГОДЕ
    chat_response = client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {
                "role": "system",
                "content": f"Сгенерируй ответ о погоде в городе {ai_response.city} на основании предоставленных данных: {str(weather_info)}",
            }
        ]
        )
    text = chat_response.choices[0].message.content
    print(text)
    await message.answer(text, parse_mode="Markdown")


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
