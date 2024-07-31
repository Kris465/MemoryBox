import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
login = os.environ['login']
password = os.environ['password']

logger.add("file.log",
           format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
           rotation='3 days', backtrace=True, diagnose=True)

url = 'https://tl.rulate.ru/'
response = requests.get(url)
if response.ok:
    with open('page.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    logger("Файл page.html сохранен")
else:
    logger("Не удалось получить код страницы")

soup = BeautifulSoup(response.text, 'html.parser')
login_field = soup.find('input', type='text', name='login[login]')
password_field = soup.find('input', type='password', name='login[pass]')

if login_field and password_field:
    login_field['value'] = login
    password_field['value'] = password

    with open('modified_page.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

    logger("Логин и пароль успешно вставлены в 'modified_page.html'.")
else:
    logger("Не удалось найти поля для логина или пароля.")
