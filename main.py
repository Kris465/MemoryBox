import os
from loguru import logger
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation='3 days', backtrace=True, diagnose=True)

    load_dotenv()
    login = os.environ['login']
    password = os.environ['password']

    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation='3 days', backtrace=True, diagnose=True)

    url = 'https://tl.rulate.ru/'
    url1 = 'https://tl.rulate.ru/register/settings'

    session = requests.Session()
    session.get(url)
    print(session.cookies)
    response = session.post(url, data={'login[login]': login, 'login[pass]': password})
    print(session.cookies)
    response1 = session.get(url1)
    print(session.cookies)

    with open('endfile.html', 'w', encoding='utf-8') as file:
        file.write(response1.text)


if __name__ == '__main__':
    main()
