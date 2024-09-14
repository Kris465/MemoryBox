import asyncio
from imaplib import Commands
import os
import json
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('TOKEN')

dp = Dispatcher()


class Form(StatesGroup):
    topic = State()
    question = State()


# Загрузка тем и вопросов из JSON файлов
def load_tests():
    tests = {}
    for filename in os.listdir('test_works'):
        if filename.endswith('.json'):
            with open(os.path.join('test_works', filename), 'r') as f:
                tests[filename[:-5]] = json.load(f)  # Имя файла без .json как ключ
    return tests


tests = load_tests()


@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer(f"Hello, {message.from_user.first_name}! Напишите /test, чтобы начать тестирование.")


@dp.message(Command("/start"))
async def start_test(message: Message):
    topics = "\n".join(tests.keys())
    await message.answer(f'Выберите тему:\n{topics}')
    await Form.topic.set()


@dp.message(state=Form.topic)
async def choose_topic(message: Message, state):
    topic = message.text.strip()
    if topic in tests:
        await state.update_data(topic=topic, rating=0, question_index=0)
        await ask_question(message.chat.id, topic, 0)
    else:
        await message.answer("Такой темы нет. Пожалуйста, выберите из списка.")


@dp.message(state=Form.question)
async def answer_question(message: Message, state):
    user_data = await state.get_data()
    topic = user_data.get('topic')
    question_index = user_data.get('question_index')

    # Получаем текущий вопрос и правильный ответ
    question_data = tests[topic][question_index]
    correct_answer = question_data['answer']

    # Проверяем ответ
    if message.text.strip().lower() == correct_answer.lower():
        rating = user_data['rating'] + 1
        await state.update_data(rating=rating)
        await message.answer("Правильно! Следующий вопрос:")
    else:
        await message.answer(f"Неправильно! Правильный ответ: {correct_answer}")
    
    # Переход к следующему вопросу или завершение теста
    if question_index + 1 < len(tests[topic]):
        await state.update_data(question_index=question_index + 1)
        await ask_question(message.chat.id, topic, question_index + 1)
    else:
        rating = user_data['rating']
        await message.answer(f"Тест завершен! Ваш рейтинг: {rating}. Напишите /test, чтобы начать снова.")
        await state.finish()

async def ask_question(chat_id, topic, question_index):
    question_data = tests[topic][question_index]
    question_text = question_data['question']
    await bot.send_message(chat_id, question_text)
    await Form.question.set()

@dp.message(lambda message: message.text.lower() == 'выход', state='*')
async def exit_test(message: Message, state):
    await state.finish()
    await message.answer("Вы вышли из теста. Напишите /test, чтобы начать снова.")

async def main():
    bot = Bot(token=API_TOKEN)
    dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
