import asyncio
import json
import logging
import os
import aiofiles
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
RATINGS_FILE = 'ratings.json'


async def load_ratings():
    if os.path.exists(RATINGS_FILE):
        async with aiofiles.open(RATINGS_FILE, 'r') as f:
            content = await f.read()
            return json.loads(content)
    return {}


def save_ratings(ratings):
    with open(RATINGS_FILE, 'w') as f:
        json.dump(ratings, f)


def update_user_score(user_id, username, test_name, score):
    ratings = load_ratings()
    if str(user_id) not in ratings:
        ratings[str(user_id)] = {"username": username, "tests": {}}
    if test_name not in ratings[str(user_id)]["tests"] or score > ratings[str(user_id)]["tests"][test_name]:
        ratings[str(user_id)]["tests"][test_name] = score
    save_ratings(ratings)


def get_user_rating(user_id):
    ratings = load_ratings()
    if str(user_id) in ratings:
        return ratings[str(user_id)]
    return None


def get_top_users(limit=10):
    ratings = load_ratings()
    sorted_users = sorted(ratings.items(), key=lambda x: sum(x[1]["tests"].values()), reverse=True)
    return [(ratings[user_id]["username"], sum(data["tests"].values())) for user_id, data in sorted_users[:limit]]


def load_test(filename):
    with open(os.path.join(TESTS_FOLDER, filename), 'r', encoding='utf-8') as file:
        return json.load(file)


def get_test_files():
    return [f for f in os.listdir(TESTS_FOLDER) if f.endswith('.json')]


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот для тестирования. Используй /topics, чтобы увидеть доступные темы, /rating для просмотра общего рейтинга или /myrating для просмотра личного рейтинга.")


@dp.message(Command("topics"))
async def cmd_topics(message: types.Message):
    test_files = get_test_files()
    if test_files:
        topics = "\n".join([f"/{os.path.splitext(f)[0]}" for f in test_files])
        await message.answer(f"Доступные темы:\n{topics}")
    else:
        await message.answer("Извините, темы пока недоступны.")


@dp.message(Command("rating"))
async def cmd_rating(message: types.Message):
    top_users = get_top_users()
    if top_users:
        rating_text = "Топ-10 пользователей:\n" + "\n".join([f"{i+1}. {username}: {score}" for i, (username, score) in enumerate(top_users)])
        await message.answer(rating_text)
    else:
        await message.answer("Рейтинг пока пуст.")


@dp.message(Command("myrating"))
async def cmd_myrating(message: types.Message):
    user_rating = get_user_rating(message.from_user.id)
    if user_rating:
        rating_text = f"Ваш рейтинг, {user_rating['username']}:\n"
        for test, score in user_rating['tests'].items():
            rating_text += f"{test}: {score}\n"
        rating_text += f"Общий счет: {sum(user_rating['tests'].values())}"
        await message.answer(rating_text)
    else:
        await message.answer("У вас пока нет рейтинга. Пройдите несколько тестов!")


@dp.message(lambda message: message.text.startswith("/") and message.text[1:] + ".json" in get_test_files())
async def start_test(message: types.Message, state: FSMContext):
    test_name = message.text[1:] + ".json"
    test_data = load_test(test_name)
    await state.set_state(TestStates.answering)
    await state.update_data(test_name=test_name, questions=test_data['questions'], question_index=0, correct_answers=0)
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
    test_name = data['test_name'].replace('.json', '')

    score = int((correct_answers / total_questions) * 100)  # Процент правильных ответов
    update_user_score(message.from_user.id, message.from_user.full_name, test_name, score)

    await message.answer(f"Тест завершен! Ваш результат: {correct_answers} из {total_questions}")
    await message.answer(f"Вы набрали {score} баллов из 100 возможных!")
    await state.clear()


async def main():
    logging.info("Запуск бота")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
