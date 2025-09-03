import json
from random import randint
import time
import requests
from bs4 import BeautifulSoup
from loguru import logger


chapters = {}
'''Stepper'''
# https://citrusaurora.com/series/that-ladys-stalker/chapter-1/


def get_novel(url):
    chapter = 1
    next_link = url
    while next_link:
        page = get_webpage(next_link)
        print(page.text)


def get_webpage(link):
    response = requests.get(link)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding
        logger.info(f"page {link} is got")
        return BeautifulSoup(response.text, 'html.parser')
    else:
        logger.error(f"page is not got: {response.status_code}")


title = input("Введите название новеллы: ")
url = input("Введите ссылку: ")
try:
    get_novel(url)
except Exception as e:
    logger.error(f"program failed with '{e}'")

with open(f'{title}.json', 'w', encoding='UTF-8') as json_file:
    loaded_data = json.dump(chapters, json_file, ensure_ascii=False)
