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
        print(links)
        chapters = {}
        for k, v in links.items():
            print(k, v)
            text = self.collect_chapter(v)
            chapter = {k: v + text}
            print(chapter)
            chapters.update(chapter)
        write(self.title, chapters, language="zh")

    def collect_chapter(self, url):
        soup = self.get_webpage(url)
        chapter = soup.find("article", class_="article-content")
        return chapter.text

    def collect_links(self, soup):
        links = {}
        raw_links = soup.find(
            "article", class_="article-content").find_all("a")
        for link in raw_links:
            href = link.get('href')
            try:
                number = re.search(r'(\d+)\.html', href).group(1)
                links.update({int(number) - 1: href})
            except AttributeError:
                continue

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
