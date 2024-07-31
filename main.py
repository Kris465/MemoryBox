import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import loguru

load_dotenv()
login = os.environ['login']
password = os.environ['password']

url = 'https://tl.rulate.ru/'
response = requests.get(url)
if response.ok:
    with open('page.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
else:
    print("Не удалось получить код страницы")

soup = BeautifulSoup(response.text, 'html.parser')
login_field = soup.find('input', type='text', name='login[login]')
password_field = soup.find('input', type='password', name='login[pass]')

if login_field and password_field:
    login_field['value'] = login
    password_field['value'] = password

    with open('modified_page.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print("Логин и пароль успешно вставлены в 'modified_page.html'.")
else:
    print("Не удалось найти поля для логина или пароля.")
