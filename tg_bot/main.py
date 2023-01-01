
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

import os
from dotenv import load_dotenv, find_dotenv

from operations import calc
from log import logwrite


load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    operation = State()


@dp.message_handler(commands = ['calc'])
async def user_register(message: types.Message):
    await message.answer("Введите, ваше выражение, пожалуйста. Формат для целых чисел 2 * 2, формат для комплексных чисел 2 + 3j: ")
    await UserState.operation.set()


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
