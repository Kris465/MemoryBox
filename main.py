import asyncio
import json
import os
from loguru import logger
from os import getenv

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    ReplyKeyboardRemove,
)

TOKEN = getenv("TOKEN")
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
form_router = Router()

RESULTS_FILE = 'results.json'


def load_tests():
    tests = []
    for filename in os.listdir('test_works'):
        if filename.endswith('.json'):
            with open(os.path.join('test_works', filename),
                      'r',
                      encoding='utf-8') as f:
                tests.extend(json.load(f))
    return tests


questions = load_tests()


def load_results():
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_results(results):
    with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)


class Form(StatesGroup):
    name = State()
    ask_question = State()
    results = State()


@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.name)
    await message.answer(
        "Привет! Как тебя зовут?",
        reply_markup=ReplyKeyboardRemove(),
    )


@form_router.message(Command("cancel"))
@form_router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    logger.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Пока-пока",
        reply_markup=ReplyKeyboardRemove(),
    )


@form_router.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text, score=0, question_index=0)
    await state.set_state(Form.ask_question)
    await ask_question(message.chat.id, 0)


async def ask_question(chat_id, question_index):
    questions_data = questions[question_index]
    await bot.send_message(chat_id, questions_data["question"])


@form_router.message(Form.ask_question)
async def process_answer(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    score = data.get("score", 0)
    current_question_index = data.get("question_index", 0)

    if current_question_index < len(questions):
        correct_answer = questions[current_question_index]["answer"]

        if message.text.casefold() == correct_answer.casefold():
            score += 1

        # Обновляем данные в состоянии
        await state.update_data(score=score,
                                question_index=current_question_index + 1)

        if current_question_index + 1 < len(questions):
            await ask_question(message.chat.id, current_question_index + 1)
        else:
            await state.set_state(Form.results)
            await show_results(message.chat.id, score)


async def show_results(chat_id, score):
    results = load_results()

    # Если ID чата уже есть в результатах, увеличиваем счет
    if str(chat_id) in results:
        results[str(chat_id)] += score
    else:
        results[str(chat_id)] = score

    save_results(results)

    await bot.send_message(
        chat_id,
        f"Тест завершен! Ваши баллы: {score}/{len(questions)}"
    )


@form_router.message(Form.results)
async def end_test(message: Message, state: FSMContext) -> None:
    await state.clear()  # Очищаем состояние


@dp.message(Command("rating"))
async def show_rating(message: Message) -> None:
    results = load_results()

    # Сортируем результаты по убыванию баллов
    sorted_results = sorted(results.items(), key=lambda item: item[1],
                            reverse=True)

    # Формируем сообщение с рейтингом
    rating_message = "Рейтинг:\n"

    for idx, (chat_id, score) in enumerate(sorted_results, start=1):
        rating_message += f"{idx}. Пользователь {chat_id}: {score} баллов\n"

    if not sorted_results:
        rating_message = "Рейтинг пуст."

    await message.answer(rating_message)


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    dp.include_router(form_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
