import json
from random import randint
import time
import requests
from bs4 import BeautifulSoup
from loguru import logger


chapters = {}
# https://www.52shuku.vip/yanqing/hyv3.html
# https://www.52shuku.vip/xiandaidushi/22547.html


def get_novel(url):
    chapter = 1
    soup = get_webpage(url)
    chapters_list = soup.find("ul", class_="list clearfix")
    elements = chapters_list.find_all("a")
    links = []
    for element in elements:
        href = element.get('href')
        if href:
            links.append(href)

    for link in links:
        chapter_page = get_webpage(link)
        text = chapter_page.find("div", class_="book_con fix")
        chapters.update({str(chapter): link + text.text})
        chapter += 1
        time.sleep(randint(1, 7))
        logger.info(f"chapter {chapter} for link {link} is got")


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
    logger.error(f"program failed with {e}")

with open(f'{title}.json', 'w', encoding='UTF-8') as json_file:
    loaded_data = json.dump(chapters, json_file, ensure_ascii=False)
