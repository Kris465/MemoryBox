from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
from dotenv import load_dotenv, find_dotenv
import logg
import game
import magic_box

load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)

async def on_startup(_):
    print("Let's play the tic-tac-toe!")

@dp.message_handler(commands = ['start'])
async def first_stage(message: types.Message):
    await bot.send_message(message.from_user.id, "Let's play the tic-tac-toe!\nWhat sign would you prefer?")

@dp.message_handler()
async def communicating(message: types.Message):
    for i in message.text:
        if i in "XO123456789":
            answer = game.controller(message.text) # (вступление, ход пользователя, ход бота)
            await message.answer(answer) # печатает ответ (поле)
            lst = magic_box.take()
            await message.answer(lst[0])
        else:
            await message.answer("Your input is wrong, try again.")
            break

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
