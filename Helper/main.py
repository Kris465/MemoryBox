import logging
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import find_dotenv, load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO)


load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ бот Инь-Ян.\n")
    chat_id = message.chat.id
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton('Кнопка 1', callback_data='button1'),
               InlineKeyboardButton('Кнопка 2', callback_data='button2'))

    await bot.send_message(chat_id, 'Выберите кнопку:', reply_markup=markup)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Это бот Инь-Ян. Я могу помочь вам с ...")


@dp.message_handler(commands=['settings'])
async def process_settings_command(message: types.Message):
    await message.reply("Здесь вы можете настроить ...")


@dp.message_handler(chat_type='private')
async def private_dialog(message: types.Message):
    await message.reply("А вот и я!")


@dp.message_handler(chat_type='supergroup')
async def goup_behaviour(message: types.Message):
    if message.text and '@Passionistabot' in message.text:
        user_id = message.from_user.id
        await bot.send_message(user_id, 'Это Я!')


class GroupBehaviour(StatesGroup):
    nice_to_meet_you = State()
    waiting_for = State()
    user_choice = State()


@dp.message_handler(chat_type='supergroup')
async def group_behaviour(message: types.Message):
    if message.text and '@Passionistabot' in message.text:
        user_id = message.from_user.id
        await bot.send_message(user_id, 'Это Я!')
        await GroupBehaviour.waiting_for.set()
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Да",
                                                callback_data="yes"),
                     types.InlineKeyboardButton(text="Нет",
                                                callback_data="no"))
        await bot.send_message(user_id, "Новелла?",
                               reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == 'yes',
                           state=GroupBehaviour.waiting_for)
async def process_novella(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(user_id, "Какую новеллу вы хотели бы прочитать?")
    await GroupBehaviour.next()


@dp.callback_query_handler(lambda c: c.data == 'no',
                           state=GroupBehaviour.waiting_for)
async def process_other(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(user_id, "Что вы хотели бы узнать или обсудить?")
    await GroupBehaviour.next()


@dp.message_handler(state=GroupBehaviour.waiting_for)
async def process_novella_text(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    novella = message.text
    await bot.send_message(user_id, f"Вы выбрали новеллу {novella}")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
