from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputFile

import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)


photo = InputFile("1_prac.png")


@dp.message_handler()
async def conversation_send(message: types.Message):
    if message.text == 'Привет':
        await bot.send_message(message.from_user.id, "И тебе привет!")
    elif message.text == 'Урок':
        await bot.send_photo(message.from_user.id, photo = photo)
    elif message.text == 'Проверка':
        await bot.send_message(message.from_user.id, "Ответы")
        
    
    # await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.answer_send(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True)

# if __name__ == 'main':
#     main()