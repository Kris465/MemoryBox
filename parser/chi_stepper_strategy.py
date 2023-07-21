import random
import time
from bs4 import BeautifulSoup

import requests
from parser.abstract_strategy import ParserStrategy
from write_to_json import write


class ChiStepper(ParserStrategy):
    def __init__(self, title, url, number=0):
        self.title = title
        self.url = url
        self.number = number

    def logic(self):
        url = self.url
        number = self.number
        all_chapters = {}
        while url is not None:
            soup = self.get_webpage(url)
            chapter = self.collect_chapter(soup)
            next_link = self.get_next_link(soup)
            temp_dict = {number: url + chapter}
            number += 1
            url = next_link
            all_chapters.update(temp_dict)
        write(self.title, all_chapters, language="zh")

    def collect_chapter(self, soup):
        chapter = soup.find("div", class_="readcontent")
        print(chapter)
        return chapter.text

    def get_next_link(self, soup):
        links = soup.find_all("a")
        for link in links:
            if "下一頁" in link.text:
                next_link = "https://www.wfxs.com.tw" + link['href']
                return next_link
            else:
                next_link = None
        return next_link

    def check(self):
        pass

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
