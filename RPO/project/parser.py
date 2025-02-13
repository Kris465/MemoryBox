import time
from loguru import logger
from random import randint

from bs4 import BeautifulSoup
import requests

from novel import Novel


class Parser:
    # https://www.52shuku.vip/yanqing/am/h2QX.html
    def __init__(self, title, url):
        self.title = title
        self.chapter = 1
        self.url = url
        self.chapters = {}
    
    def get_novel(self):
        soup = self.get_webpage(self.url)
        chapters_list = soup.find("ul", class_="list clearfix")
        elements = chapters_list.find_all("a")
        links = []
        for element in elements:
            href = element.get('href')
            if href:
                links.append(href)

        for link in links:
            chapter_page = self.get_webpage(link)
            text = chapter_page.find("div", class_="book_con fix")
            self.chapters.update({str(self.chapter): link + text.text})
            self.chapter += 1
            time.sleep(randint(1, 7))
            logger.info(f"chapter {self.chapter} for link {link} is got")
            
        novel = Novel(self.title)
        logger.info(f"novel is created {self.title}")
        novel.write_novel_to_db(self.chapters)
        logger.info(f"novel is written to the json {self.title}")
    
    def get_webpage(self, link):
        response = requests.get(link)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            logger.info(f"page {link} is got")
            return BeautifulSoup(response.text, 'html.parser')
        else:
            logger.error(f"page is not got: {response.status_code}")
    