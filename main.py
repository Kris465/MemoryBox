import os
from bot import Bot
from loguru import logger
import requests
# from bs4 import BeautifulSoup
from dotenv import load_dotenv


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation='3 days', backtrace=True, diagnose=True)

    load_dotenv()
    login = os.environ['login']
    password = os.environ['password']

    url = 'https://tl.rulate.ru/'

    session = requests.Session()
    session.get(url)
    session.post(url, data={'login[login]': login, 'login[pass]': password})
    bot = Bot(session)
    bot.get_all_chapters()
    bot.update_chapters()


if __name__ == '__main__':
    main()
