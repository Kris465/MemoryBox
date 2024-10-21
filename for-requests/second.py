import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from loguru import logger
import requests

from dotenv import load_dotenv


url = 'https://tl.rulate.ru/register/settings'

load_dotenv()
login = os.getenv("login")
password = os.getenv("password")

logger.add("file.log",
           format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
           rotation='3 days', backtrace=True, diagnose=True)

session = requests.Session()
response = session.get(url)
if response.ok:
    logger.info("Получена страница для логина.")
else:
    logger.error("Не удалось получить код страницы для логина.")

soup = BeautifulSoup(response.text, 'html.parser')

login_field = soup.find('input', attrs={'name': 'login[login]'})
password_field = soup.find('input', attrs={'name': 'login[pass]'})

if login_field and password_field:
    login_field['value'] = login
    password_field['value'] = password

    form_action = urljoin(url, soup.find('form')['action'])

    data = {
        'login[login]': login,
        'login[pass]': password
    }

    response = session.post(form_action, data=data)

    if response.ok:
        logger.info("Успешный вход в систему.")
    else:
        logger.error(f"Ошибка входа: {response.text}")
else:
    logger.error("Не удалось найти поля для логина или пароля.")

with open("output.html", "w", encoding="utf-8") as file:
    file.write(response.text)
