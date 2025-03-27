from aiogram import Dispatcher, types, F
from aiogram.filters import Command
from loguru import logger


def setup_private_handlers(dp: Dispatcher):
    @dp.message(Command('start'), F.chat.type == "private")
    async def private_start(message: types.Message):
        await message.answer("Привет! Это бот для личных сообщений")
        logger.info(f"ЛС: {message.from_user.id} начал чат")

    @dp.message(F.chat.type == "private")
    async def private_echo(message: types.Message):
        await message.answer(f"Вы написали в ЛС: {message.text}")
        logger.info(f"ЛС: эхо для {message.from_user.id}")
