import requests
from bs4 import BeautifulSoup
from loguru import logger

url = input("Введите ссылку: ")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Wind64; x64) AppWebKit/537.36 (KHTML, like Geco) Chrome/120.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.text)
