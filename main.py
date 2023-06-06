from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from controller import Controller
from view import View
import os
from dotenv import find_dotenv, load_dotenv


def main():
    load_dotenv(find_dotenv())
    TOKEN = os.environ.get('TOKEN')
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)
    view = View()
    controller = Controller(dp, view)
    controller.test()
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
