
from bs4 import BeautifulSoup
import requests

from writer_to_json import write


def one_chapter():
    url = input("url: ")
    number = input("chapter: ")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    print(response.status_code)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    chapter_text = soup.find('div', class_="container").text
    print(chapter_text)
    write(number, {number: chapter_text}, language="chi")


one_chapter()
