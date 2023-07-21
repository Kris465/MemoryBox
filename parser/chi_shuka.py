import random
import re
import time
from bs4 import BeautifulSoup

import requests
from parser.abstract_strategy import ParserStrategy
from write_to_json import write


class ChiShuka(ParserStrategy):

    def __init__(self, title, project_webpage, number=0):
        self.title = title
        self.project_webpage = project_webpage
        self.number = number

    def logic(self):
        soup = self.get_webpage(self.project_webpage)
        links = self.collect_links(soup)
        chapters = {}
        for k, v in links.items():
            text = self.collect_chapter(v)
            chapter = {k: text}
            print(chapter)
            chapters.update(chapter)
        write(self.title, chapters, language="zh")

    def collect_chapter(self, url):
        soup = self.get_webpage(url)
        chapter = soup.find("div", class_="book_con fix")
        return chapter.text

    def collect_links(self, soup):
        # Регулярка
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith("https://www.52shuku.vip/yanqing/b/h7vv"):
                links.append(href)

        sorted_links = sorted(set(links))
        links = {str(i): link for i, link in enumerate(sorted_links)}
        return links

    def get_webpage(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
        time.sleep(random.randint(10, 40))
        response = requests.get(url, headers=headers)
        print(response.status_code)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
