import asyncio
import json
import logging
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.methods import DeleteWebhook
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

TESTS_FOLDER = 'tests'


def load_test(filename):
    with open(os.path.join(TESTS_FOLDER, filename), 'r', encoding='utf-8') as file:
        test_data = json.load(file)
        return test_data


def get_test_files():
    return [f for f in os.listdir(TESTS_FOLDER) if f.endswith('.json')]


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот, который расскажет какие вопросы будут на тестировании. Используй /topics, чтобы увидеть список тем и подготовится. Удачи ;)")


@dp.message(Command("topics"))
async def cmd_topics(message: types.Message):
    test_files = get_test_files()
    if test_files:
        topics = "\n".join([f"/{os.path.splitext(f)[0]}" for f in test_files])
        await message.answer(f"Доступные темы:\n{topics}")
    else:
        await message.answer("Извините, темы пока недоступны.")


@dp.message(lambda message: message.text.startswith("/") and message.text[1:] + ".json" in get_test_files())
async def send_random_question(message: types.Message):
    test_name = message.text[1:] + ".json"
    test_data = load_test(test_name)
    random_question = random.choice(test_data['questions'])
    await message.answer(f"Вопрос: {random_question['question']}")


@dp.message()
async def handle_unknown_command(message: types.Message):
    await message.answer("Выберите тему, и я задам случайный вопрос по ней.")


async def main():
    logging.info("Запуск бота")
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
