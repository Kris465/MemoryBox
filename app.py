import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = '7340430032:AAHtNiOBYzJ7-xMTMHoRSlJqBWseDihsWQM'
bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)
    await message.reply(message.text)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
