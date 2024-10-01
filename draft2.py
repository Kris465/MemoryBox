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

# Здесь создать функцию для считывания вопросв тестов из папки



class Form(StatesGroup):
    name = State()
    ask_question = State()
    results = State()

<<<<<<< HEAD:draft2.py

def load_tests():
    tests = {}
    for filename in os.listdir('test_works'):
        if filename.endswith('.json'):
            with open(os.path.join('test_works', filename), 'r') as f:
                tests[filename[:-5]] = json.load(f)
    return tests


tests = load_tests()


@dp.message(Command("/start"))
async def start_test(message: Message):
    topics = "\n".join(tests.keys())
    await message.answer(f'Выберите тему:\n{topics}')
    await Form.topic.set()


@form_router.message(StateFilter(Form.topic))
async def choose_topic(message: Message, state: FSMContext):
    topic = message.text.strip()
    if topic in tests:
        await state.update_data(topic=topic, rating=0, question_index=0)
        await ask_question(message.chat.id, topic, 0)
    else:
        await message.answer("Такой темы нет. Пожалуйста, выберите из списка.")


async def ask_question(chat_id, topic, question_index):
    question_data = tests[topic][question_index]
    question_text = question_data['question']

    # Создаем инлайн-клавиатуру для вариантов ответов
    keyboard = InlineKeyboardMarkup(row_width=2)
    for idx, option in enumerate(question_data['options']):
        button = InlineKeyboardButton(text=option, callback_data=f"answer_{idx}")
        keyboard.add(button)

    await bot.send_message(chat_id, question_text, reply_markup=keyboard)
    await Form.question.set()


@form_router.callback_query(lambda c: c.data.startswith('answer_'))
async def answer_question(callback_query, state: FSMContext):
    user_data = await state.get_data()
    topic = user_data.get('topic')
    question_index = user_data.get('question_index')

    # Получаем текущий вопрос и правильный ответ
    question_data = tests[topic][question_index]
    correct_answer_index = question_data['answer_index']  # Индекс правильного ответа
=======

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

>>>>>>> refs/remotes/origin/main:main.py

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
<<<<<<< HEAD:draft2.py
    await bot.delete_webhook(drop_pending_updates=True)
=======
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    dp.include_router(form_router)

>>>>>>> refs/remotes/origin/main:main.py
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
