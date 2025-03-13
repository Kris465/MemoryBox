import os
from random import randint
import asyncio
from loguru import logger
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days", backtrace=True, diagnose=True)

    bot = Bot(TOKEN)
    logger.info("Бот создан")
    dp = Dispatcher()
    logger.info("Диспетчер создан")

    async def send_random_number():
        while True:
            try:
                random_number = randint(1, 1000)
                await bot.send_message(CHANNEL_ID,
                                       f"Случайное число: {random_number}")
                logger.info(f"Отправлено число: {random_number}")
            except Exception as e:
                logger.error(f"Ошибка при отправке сообщения: {e}")
            await asyncio.sleep(30)

    @dp.message(Command("start"))
    async def start_command(message: types.Message):
        await message.answer(
            "Бот запущен! Случайные числа будут отправляться в канал.")

    task = asyncio.create_task(send_random_number())

    try:
        await dp.start_polling(bot)
    finally:
        task.cancel()
        await bot.session.close()
        logger.info("Бот остановлен")


if __name__ == '__main__':
    asyncio.run(main())
