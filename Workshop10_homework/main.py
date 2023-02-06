from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
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

