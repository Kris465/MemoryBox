from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
from dotenv import load_dotenv, find_dotenv
import logg
import game

load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
user_sign = "l"
my_sign = "l"
win = False

async def on_startup(_):
    print("Let's play the tic-tac-toe!")

@dp.message_handler(commands = ['start'])
async def first_stage(message: types.Message):
    await bot.send_message(message.from_user.id, "Let's play the tic-tac-toe!\nWhat sign would you prefer?")

@dp.message_handler()
async def communicating(message: types.Message):
    


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)