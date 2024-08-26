import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from loguru import logger
import requests


class BotUpdator:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.base_url = 'https://tl.rulate.ru/'
        self.chapters = []  # Список для хранения ссылок на главы

    def login(self):
        load_dotenv()
        login = os.environ['login']
        password = os.environ['password']

        # Получаем страницу для аутентификации
        response = self.session.get(self.base_url)
        if response.ok:
            logger.info("Получена страница для логина.")
        else:
            logger.error("Не удалось получить код страницы для логина.")
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        # Заполняем поля логина и пароля
        login_field = soup.find('input', attrs={'name': 'login[login]'})
        password_field = soup.find('input', attrs={'name': 'login[pass]'})

        if login_field and password_field:
            login_field['value'] = login
            password_field['value'] = password

            form_action = soup.find('input').attrs['action']

            # Создаем данные для отправки
            data = {
                'login[login]': login,
                'login[pass]': password
            }

            # БАГ ЗДЕСЬ!!!
            response = self.session.post(form_action, data=data)

            if response.ok:
                logger.info("Успешный вход в систему.")
            else:
                logger.error("Ошибка входа.")
                return
        else:
            logger.error("Не удалось найти поля для логина или пароля.")

    def fetch_chapters(self):
        # Здесь вы можете добавить логику для получения ссылок на главы
        # Например, можно парсить главную страницу новеллы
        response = self.session.get(self.base_url + 'book/95179')
        if response.ok:
            logger.info("Получены главы новеллы.")
            soup = BeautifulSoup(response.text, 'html.parser')
            self.chapters = [a['href'] for a in soup.find_all(
                'a', class_='chapter_row')]
            print(self.chapters)
        else:
            logger.error("Не удалось получить главы новеллы.")

    def update_chapters(self):
        for chapter in self.chapters:
            response = self.session.get(chapter)
            if response.ok:
                logger.info(f"Получена глава: {chapter}")
                # Здесь можно обработать или сохранить содержимое главы
                with open(f"{chapter.split('/')[-1]}.html",
                          'w',
                          encoding='utf-8') as file:
                    file.write(response.text)
            else:
                logger.error(f"Ошибка при получении главы: {chapter}")
