import asyncio
import os
import json
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command, StateFilter
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
form_router = Router()
dp.include_router(form_router)

class Form(StatesGroup):
    topic = State()
    question = State()

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

    # Проверяем ответ
    selected_answer_index = int(callback_query.data.split('_')[1])
    if selected_answer_index == correct_answer_index:
        rating = user_data['rating'] + 1
        await state.update_data(rating=rating)
        await callback_query.answer("Правильно! Следующий вопрос:")
    else:
        await callback_query.answer(f"Неправильно! Правильный ответ: {question_data['options'][correct_answer_index]}")

    # Переход к следующему вопросу или завершение теста
    if question_index + 1 < len(tests[topic]):
        await state.update_data(question_index=question_index + 1)
        await ask_question(callback_query.from_user.id, topic, question_index + 1)
    else:
        rating = user_data['rating']
        await callback_query.message.answer(f"Тест завершен! Ваш рейтинг: {rating}. Напишите /start, чтобы начать снова.")
        await state.finish()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
