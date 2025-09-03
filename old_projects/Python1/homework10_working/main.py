from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from dotenv import load_dotenv, find_dotenv
import game
import os

load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)
game_list = []
choose = ""

async def on_startup(_):
    print("Let's play the tic-tac-toe!")

@dp.message_handler(commands = ['start'])
async def first_stage(message: types.Message):
    global game_list
    game_list = list(range(1, 10))
    await bot.send_message(message.from_user.id, "Let's play the tic-tac-toe!\nWhat sign would you prefer?")

@dp.message_handler()
async def communicating(message: types.Message):
    global game_list, choose

    if message.text in 'XO':
        choose = message.text
        answer = game.controller(message.text, choose, game_list)
        await message.answer(f"Move {answer}. Enter a position")
    if message.text in '123456789':
        answer = game.controller(message.text, choose, game_list)
        await message.answer(answer)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
