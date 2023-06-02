from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

import os
from dotenv import load_dotenv, find_dotenv

from controller import Controller


load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    title = State()
    action = State()


@dp.message_handler(commands = ['start'])
async def user_register(message: types.Message):
    await message.answer("Какой проект ищем?")
    await UserState.title.set()


@dp.message_handler(state=UserState.operation)
async def get_useroperation(message: types.Message, state: FSMContext):
    await state.update_data(useroperation = message.text)
    logwrite("User input: ", message.text)
    await message.answer("Отлично! Считаем!")
    data = await state.get_data()
    answer = calc(data)
    await message.answer(f'Ваш ответ: {answer}')
    logwrite("Answer: ", answer)

    await state.finish()

executor.start_polling(dp, skip_updates=True)
