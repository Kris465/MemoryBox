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

async def on_startup(_):
    print("Let's play the tic-tac-toe!")

@dp.message_handler(commands = ['start'])
async def first_stage(message: types.Message):
    await bot.send_message(message.from_user.id, "Let's play the tic-tac-toe!\nWhat sign would you prefer?")

@dp.message_handler()
async def communicating(message: types.Message):
    temp_board = board
    for i in message.text:
        if i in "XO123456789":
            answer, temp_board = game.controller(message.text, temp_board) # (вступление, ход пользователя, ход бота)
            await message.answer(answer) # печатает ответ (поле)
            await message.answer(temp_board)
        else:
            await message.answer("Your input is wrong, try again.")
            break

    # if isinstance(answer, list):
    #     temp_board = answer[1]

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
