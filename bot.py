import os

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from loguru import logger
import requests


class BotUpdator:
    def __init__(self) -> None:
        pass

    def login(self):
        load_dotenv()
        login = os.environ['login']
        password = os.environ['password']
        url = 'https://tl.rulate.ru/'
        response = requests.get(url)
        if response.ok:
            with open('page.html', 'w', encoding='utf-8') as file:
                file.write(response.text)
            logger.info("Файл page.html сохранен")
        else:
            logger.error("Не удалось получить код страницы")

        soup = BeautifulSoup(response.text, 'html.parser')

        login_field = soup.find('input', attrs={'name': 'login[login]'})
        password_field = soup.find('input', attrs={'name': 'login[pass]'})

        if login_field and password_field:
            login_field['value'] = login
            password_field['value'] = password

            with open('modified_page.html', 'w', encoding='utf-8') as file:
                file.write(str(soup))

            logger.info(
                "Логин и пароль успешно вставлены в 'modified_page.html'.")
        else:
            logger.error("Не удалось найти поля для логина или пароля.")

        with open('modified_page.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

        response = requests.post(url,
                                 data=html_content,
                                 headers={'Content-Type': 'text/html'})

        with open('endfile.html', 'w', encoding='utf-8') as file:
            file.write(response.text)

    def update(self):
        pass
