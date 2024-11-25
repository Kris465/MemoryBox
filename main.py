import asyncio
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


# Определяем состояния для FSM (Finite State Machine)
class TestStates(StatesGroup):
    answering = State()


# Список вопросов и правильных ответов
questions = [
    {"question": "Столица Франции?", "answer": "Париж"},
    {"question": "2 + 2 = ?", "answer": "4"},
    {"question": "Самая длинная река в мире?", "answer": "Нил"}
]


@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(TestStates.answering)
    await state.update_data(question_index=0, correct_answers=0)
    await ask_question(message, state)
    await message.answer("Начинаем тест!")


async def ask_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    question_index = data['question_index']

    if question_index < len(questions):
        question = questions[question_index]['question']
        await message.answer(f"Вопрос {question_index + 1}: {question}")
    else:
        await finish_test(message, state)


@dp.message(TestStates.answering)
async def process_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()
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
    total_questions = len(questions)

    await message.answer(f"Тест завершен! Ваш результат: {correct_answers} из {total_questions}")
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
