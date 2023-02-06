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
import check

load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    userstring = State()


@dp.message_handler(commands = ['calc'])
async def user_register(message: types.Message):
    await message.answer("Hello! What would you like to count?")
    logg.logging.debug("Program starts")
    await message.answer("Please, write your statement: ")
    await UserState.userstring.set()


@dp.message_handler(state=UserState.userstring)
async def get_userstring(message: types.Message, state: FSMContext):
    await state.update_data(userstring = message.text)
    user_dict = await state.get_data()   
    current = str(user_dict.get('userstring'))
    logg.logging.debug(f"User's unput has got. {current}")
    answer = "nothing"

    if current == None:
        answer = "Try again."
    else:
        correct_in = check.checking(current)
        data = current.split()
        if isinstance(correct_in, str):
            answer = correct_in
        elif correct_in:
            if "s" in current:
                data = check.pow_remake(data)
                answer = mod1.calculator(mod1.cut(data))
            else: answer = mod1.calculator(mod1.cut(data))   
        else:
            answer = mod2.calculator(mod2.cut(data))

    await message.answer(f'Your answer: {answer}')

    await state.finish()

executor.start_polling(dp, skip_updates=True)
