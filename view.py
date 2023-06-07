import os
from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv


class View:
    def __init__(self):
        self.bot = self.get_bot()
        self.dp = Dispatcher(self.bot)

    def get_bot(self):
        load_dotenv(find_dotenv())
        token = os.environ.get('TOKEN')
        bot = Bot(token)
        return bot

    async def start(self, message: types.Message):
        chat_id = message.chat.id
        await self.bot.send_message(chat_id=chat_id, text='Привет, я бот!')

    async def show_message(self, message):
        await self.bot.send_message(chat_id=chat_id, text=message)

    async def get_user_input(self):
        message = await self.bot.send_message(chat_id=chat_id, text='Введите имя пользователя:')
        nickname = await self.dp.wait_for(types.Message(text='nickname'))
        message = await self.bot.send_message(chat_id=chat_id, text='Введите возраст пользователя:')
        name = await self.dp.wait_for(types.Message(text='name'))

        return nickname.text, name.text
