import asyncio
import json
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class TestStates(StatesGroup):
    answering = State()


TESTS_FOLDER = 'tests'


def load_test(filename):
    with open(os.path.join(TESTS_FOLDER, filename), 'r', encoding='utf-8') as file:
        return json.load(file)


def get_test_files():
    return [f for f in os.listdir(TESTS_FOLDER) if f.endswith('.json')]


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот для тестирования. Используй /topics, чтобы увидеть доступные темы.")


@dp.message(Command("topics"))
async def cmd_topics(message: types.Message):
    test_files = get_test_files()
    if test_files:
        topics = "\n".join([f"/{os.path.splitext(f)[0]}" for f in test_files])
        await message.answer(f"Доступные темы:\n{topics}")
    else:
        await message.answer("Извините, темы пока недоступны.")


@dp.message(lambda message: message.text.startswith("/") and message.text[1:] + ".json" in get_test_files())
async def start_test(message: types.Message, state: FSMContext):
    test_name = message.text[1:] + ".json"
    test_data = load_test(test_name)
    await state.set_state(TestStates.answering)
    await state.update_data(questions=test_data['questions'], question_index=0, correct_answers=0)
    await message.answer(f"Начинаем тест по теме '{test_data['name']}'!")
    await ask_question(message, state)


async def ask_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    questions = data['questions']
    question_index = data['question_index']

    if question_index < len(questions):
        question = questions[question_index]['question']
        await message.answer(f"Вопрос {question_index + 1}: {question}")
    else:
        await finish_test(message, state)


@dp.message(TestStates.answering)
async def process_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()
    questions = data['questions']
    question_index = data['question_index']
    correct_answers = data['correct_answers']

    if questions[question_index]['answer'].lower() == message.text.lower():
        correct_answers += 1
        await message.answer("Правильно!")
    else:
        await message.answer(f"Неправильно. Правильный ответ: {questions[question_index]['answer']}")

    await state.update_data(question_index=question_index + 1, correct_answers=correct_answers)
    await ask_question(message, state)


async def finish_test(message: types.Message, state: FSMContext):
    data = await state.get_data()
    correct_answers = data['correct_answers']
    total_questions = len(data['questions'])

    await message.answer(f"Тест завершен! Ваш результат: {correct_answers} из {total_questions}")
    await state.clear()


async def main():
    logging.info("Запуск бота")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
