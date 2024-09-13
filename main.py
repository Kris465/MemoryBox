import asyncio
# import json
import os
# import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from dotenv import load_dotenv


load_dotenv()
API_TOKEN = os.getenv('TOKEN')

dp = Dispatcher()


class Form(StatesGroup):
    

@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer(f"Hello, {message.from_user.id}!")


@dp.message()
async def echo_message(message: Message):
    await message.answer(message.text)


async def main():
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
