import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from loguru import logger
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

logger.add('bot.log', rotation='10 MB')


@dp.message()
async def echo_message(message: types.Message):
    user_id = message.from_user.id
    text = message.text

    logger.info(f"Пользователь {user_id}: {text}")

    await message.answer(text)


async def main():
    logger.info("Бот запущен")

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Ошибка бота: {e}")
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
