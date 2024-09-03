import os
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from handlers import register_handlers


load_dotenv()
TOKEN = os.getenv('API_TOKEN')
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def on_startup(dp):
    pass

if __name__ == '__main__':
    register_handlers(dp)
    executor.start_polling(dp, on_startup=on_startup)
