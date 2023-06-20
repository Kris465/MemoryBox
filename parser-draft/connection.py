import random
import time
from bs4 import BeautifulSoup

import requests


def connection(url, tag='div', cl='entry-content',
               language='en',
               urls=False):
    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/111.0.0.0 Safari/537.36'}

    response = requests.get(url, headers=headers)
    print(response.status_code)
    if language == "zh":
        response.encoding = response.apparent_encoding
        time.sleep(random.randint(10, 120))
        soup = BeautifulSoup(response.text, 'html.parser')
        if urls:
            links = soup.find_all('a')
            return links
        else:
            text = soup.find_all(tag, cl)
            return text
    else:
        time.sleep(10)
        soup = BeautifulSoup(response.text, "lxml")
        if urls:
            links = soup.find_all('a')
            return links
        else:
            text = soup.find_all(tag, cl)
            if text[0].text == text[-1].text:
                return text[0]
            return text
