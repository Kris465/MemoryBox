import asyncio
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

questions = [
    {"question": "Что такое Python?", "answer": "язык программирования"},
    {"question": "Что такое переменная?", "answer": "хранение данных"},
    # Добавьте больше вопросов по мере необходимости
]


class Form(StatesGroup):
    name = State()
    ask_question = State()
    results = State()


@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.name)
    await message.answer(
        "Привет! Как зовут?",
        reply_markup=ReplyKeyboardRemove(),
    )


@form_router.message(Command("cancel"))
@form_router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
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
    await state.update_data(name=message.text, score=0)
    await state.set_state(Form.ask_question)
    await ask_question(message.chat.id, 0, state)


async def ask_question(chat_id, question_index, state: FSMContext):
    questions_data = questions[question_index]
    await bot.send_message(chat_id, questions_data["question"])


@form_router.message(Form.ask_question)
async def process_answer(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    score = data.get("score", 0)

    current_question_index = score

    if current_question_index < len(questions):
        correct_answer = questions[current_question_index]["answer"]

        if message.text.casefold() == correct_answer.casefold():
            score += 1  # Увеличиваем счет за правильный ответ

        await state.update_data(score=score)  # Сохраняем текущий счет

        if current_question_index + 1 < len(questions):
            await ask_question(message.chat.id,
                               current_question_index + 1,
                               state)  # Задаем следующий вопрос
        else:
            await state.set_state(Form.results)  # Переходим к результатам
            await show_results(message.chat.id, score)  # Показываем результаты


async def show_results(chat_id, score):
    await bot.send_message(
        chat_id,
        f"Тест завершен! Ваши баллы: {score}/{len(questions)}")


@form_router.message(Form.results)
async def end_test(message: Message, state: FSMContext) -> None:
    await state.clear()  # Очищаем состояние


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    dp.include_router(form_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
