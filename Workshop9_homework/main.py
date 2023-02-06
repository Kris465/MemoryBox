from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

import os
from dotenv import load_dotenv, find_dotenv

import logg
import mod1
import mod2

load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    operation = State()

@dp.message_handler(commands = ['calc'])
async def user_register(message: types.Message):
    await message.answer("Hello! What would you like to count?")
    logg.logging.debug("Program starts")
    await message.answer("Input your statement usually: -2 + 3. \nFor addition: '+' \nFor subtraction: '-' \nFor multiplication: '*' \nFor divining: '/' \nFor divining without  fraction: '//' \nFor fraction from divining: '%' \nFor power: '**' \nFor square root put 's' before the number.\nFor complex numbers you shoul use: -2+3j. Without spaces inside the number. If you don't have any value before j, you should put 1, like: 6+1j.")
    await message.answer("Don't forget to separate '(' and ')' with spaces.\n")

@dp.message_handler(state=UserState.operation)
async def get_useroperation(message: types.Message, state: FSMContext):
    correct_in = "everything is OK?"

    while isinstance(correct_in, str):
        await message.answer("Please, input your statement: ")
        await state.update_data(useroperation = message.text)
        use_lst = await state.get_data()
        logg.logging.debug("User's unput has got.")
        correct_in = check(use_lst)

    if correct_in:
        answer = mod1(use_lst)
    else:
        answer = mod1(use_lst)

    await message.answer(f'Ваш ответ: {answer}')

    await state.finish()

executor.start_polling(dp, skip_updates=True)
