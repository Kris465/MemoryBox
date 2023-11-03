import random
import time
import re
from bs4 import BeautifulSoup
import requests
from parser.abstract_strategy import ParserStrategy
from write_to_json import write


class Zg(ParserStrategy):

    # https://www.82zg.com/book/25485/
    def __init__(self, title, project_webpage):
        self.title = title
        self.project_webpage = project_webpage

    def logic(self):
        links = self.collect_links()
        write(self.title, links, "zh")
        chapters = {}
        for chapter, link in links.items():
            time.sleep(random.randint(10, 30))
            text = self.collect_chapter(link.strip())
            match = re.search(r'\d+', chapter)
            chapter = {match.group(0):
                       chapter + "/n" + link + text}
            chapters.update(chapter)

        write(self.title, chapters, "zh")

    def collect_chapter(self, url):
        page = self.get_webpage(url)
        print(url)
        text = page.find("div", id="content").text
        return text

    def collect_links(self):
        page = self.get_webpage(self.project_webpage)
        links = {link.text: 'https://www.82zg.com' + link.get("href")
                 for link in page.find('div', id='list').find_all("a")}
        return links

    def get_next_link(self):
        pass

    def get_webpage(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        print(response.status_code)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def check(self):
        pass
