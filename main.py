import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import find_dotenv, load_dotenv
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


logging.basicConfig(level=logging.INFO)


load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nКак зовут?\n")


@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)

# создаем кнопку
    button = InlineKeyboardButton("Нажми меня", callback_data="button_pressed")

# создаем клавиатуру и добавляем на нее кнопку
    keyboard = InlineKeyboardMarkup().add(button)

# отправляем сообщение с клавиатурой
    await bot.send_message(chat_id, "Выберите действие:", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
