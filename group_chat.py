import random
from aiogram import Router, types
from aiogram.filters import Command
from loguru import logger


group_router = Router()


group_games = {}


@group_router.message(Command('start_game'))
async def start_game(message: types.Message):
    chat_id = message.chat.id
    group_games[chat_id] = random.randint(1, 100)
    await message.answer("Я загадал число от 1 до 100. Попробуй угадать!")
    logger.info(f"Игра начала в чате {chat_id}")


@group_router.message(Command('guess'))
async def make_guess(message: types.Message):
    chat_id = message.chat.id
    if chat_id not in group_games:
        await message.answer("Сначала начинте игру с помощью /start_game")
        return

    secret_number = group_games[chat_id]

    try:
        guess = int(message.text.split()[1])
    except (IndexError, ValueError):
        await message.answer("Используйте команду так: /guess <число>")

    if guess < secret_number:
        await message.answer("Мое число больше!")
    elif guess > secret_number:
        await message.answer("Мое число меньше!")
    else:
        await message.answer(f"Поздравляем! Вы угадали число {secret_number}!")
        del group_games[chat_id]
        logger.info(f"Игра заверешена в чате {chat_id}")
