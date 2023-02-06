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
    await message.answer("Input your statement usually: -2 + 3. \nFor addition: '+' \nFor subtraction: '-' \nFor multiplication: '*' \nFor divining: '/' \nFor divining without  fraction: '//' \nFor fraction from divining: '%' \nFor power: '**' \nFor square root put 's' before the number.\nFor complex numbers you shoul use: -2+3j. Without spaces inside the number. If you don't have any value before j, you should put 1, like: 6+1j.")
    await message.answer("Don't forget to separate '(' and ')' with spaces.\n")
    await message.answer("Please, input your statement: ")
    await UserState.operation.set()

@dp.message_handler(state=UserState.userstring)
async def get_statement(message: types.Message, state: FSMContext):
    await state.update_data(userstring = message.text)
    correct_in = "everything is OK?"
    user_dict = await state.get_data()
    user_string = user_dict['userstring']

    print(user_string, type(user_string))

    logg.logging.debug("User's unput has got.")
    correct_in = check.checking(str(use_lst))

    print(correct_in)
    
    if isinstance(correct_in, str):
        await message.answer("Your input is incorrect. Try again, please:")
    else:
        oper_lst = str(use_lst).split()
        print(oper_lst)

    if correct_in:
        temp = mod1.cut(oper_lst)
        answer = mod1.calculator(temp)
    else:
        temp = mod2.cut(oper_lst)
        answer = mod2.calculator(temp)

    await message.answer(f'Your answer: {answer}')

    await state.finish()

executor.start_polling(dp, skip_updates=True)
