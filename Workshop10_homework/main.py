from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
from dotenv import load_dotenv, find_dotenv
import logg

load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)

async def on_startup(_):
    print("Let's play the tic-tac-toe!")

@dp.message_handler()
async def communicating(message: types.Message):
    if message.text == "Привет": 
        await message.answer("И тебе привет!")
    




executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
