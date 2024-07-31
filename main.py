import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
login = os.environ['login']
password = os.environ['password']

url = 'https://tl.rulate.ru/'
response = requests.get(url)
if response.ok:
    with open('page.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("Файл сохранен")
else:
    print("Не удалось получить код страницы")

soup = BeautifulSoup(response.text, 'html.parser')
login_field = soup.find('div', class_='main-header-avatar').find(
    'input', name=login)
print(login_field)
