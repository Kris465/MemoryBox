from aiogram import Bot, executor, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

import os
from dotenv import load_dotenv, find_dotenv
import logg

load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    user_choice = State()
    humanstep = State()
    mystep = State()
    showresults = State()


@dp.message_handler(commands=['play'])
async def user_choice(message: types.Message):
    await message.answer("Choose your sign, please.")
    await UserState.user_choice.set()

    if sign in "XO":
        await message.answer("Thank you! Let's play!")
        if sign == "X":
            flag_ = True
        else: flag_ = False
    else: 
        await UserState.user_choice.set()
        await message.answer("Try again.")

    steps = 1

    while steps < 9:
        if flag_ == True:
            await UserState.humanstep.set()
        else: await UserState.mystep.set()

@dp.message_handler(state=UserState.user_choice)
async def get_userchoice(message: types.Message, state: FSMContext):
    await state.update_data(userchoice=message.text)
    us_sign = await state.get_data()
    global sign = str(us_sign.get('userchoice'))
    

