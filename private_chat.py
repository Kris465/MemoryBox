from aiogram import Router, types
from aiogram.filters import Command
from loguru import logger


private_router = Router()


@private_router.message(Command('start'))
async def private_start(message: types.Message):
    await message.answer("Привет! Я эхо-бот. Просто напиши мне что-нибудь!")
    logger.info(f"Пользователь {message.from_user.id} начал чат")


@private_router.message()
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")
    logger.info(f"Эхо для пользователя {message.from_user.id}: {message.text}")
