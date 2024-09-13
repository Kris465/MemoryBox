import json
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('TOKEN')

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# FSM
class Form:
    topic = "topic"
    question = "question"


# Функция для загрузки тестов из папки
def load_tests():
    tests = {}
    for filename in os.listdir('tests'):
        if filename.endswith('.json'):
            tests[filename[:-5]] = filename  # Убираем .json из названия файла
    return tests


# Функция для сохранения результатов пользователей
def save_user_results(user_id, topic, score):
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            users = json.load(f)
    else:
        users = {}

    users[str(user_id)] = {'topic': topic, 'score': score}

    with open('users.json', 'w') as f:
        json.dump(users, f)


# Команда /start
@dp.message(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я бот для тестирования студентов. Используй команду /topics, \
            чтобы увидеть доступные тесты.")


# Команда /topics
@dp.message(commands=['topics'])
async def cmd_topics(message: types.Message):
    tests = load_tests()
    topics_list = "\n".join(tests.keys())
    await message.answer(f"Доступные темы:\n{topics_list}")


# Обработка выбора темы
@dp.message(lambda message: message.text in load_tests().keys())
async def choose_topic(message: types.Message, state: FSMContext):
    topic = message.text
    with open(f'tests/{load_tests()[topic]}', 'r') as f:
        questions = json.load(f)

    random.shuffle(questions)  # Рандомизируем вопросы
    score = 0

    for question in questions:
        await message.answer(question['question'])
        answer = await bot.wait_for(types.Message)

        if answer.text.lower() == question['answer'].lower():
            score += 1

    save_user_results(message.from_user.id, topic, score)
    await message.answer(f"Тест завершен! Ваши баллы: {score}")


# Команда /rating
@dp.message(commands=['rating'])
async def cmd_rating(message: types.Message):
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            users = json.load(f)

        rating_list = "\n".join(
            [f"ID: {user_id}, Тема: {data['topic']}, Баллы: {data['score']}"
                for user_id, data in users.items()])
        await message.answer(f"Рейтинг пользователей:\n{rating_list}")
    else:
        await message.answer("Нет данных о пользователях.")

if __name__ == '__main__':
    asyncio.run(main())
