from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
token = os.environ.get('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def conversation_send(message: types.Message):
    if message.text == 'Привет':
        await bot.send_message(message.from_user.id, "И тебе привет!")

    # await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.answer_send(message.from_user.id, message.text)



executor.start_polling(dp, skip_updates=True)


# if __name__ == 'main':
#     main()