import re
from bs4 import BeautifulSoup
import requests
from parser.abstract_strategy import ParserStrategy
from write_to_json import write


class Wx256(ParserStrategy):

    def __init__(self, title, project_webpage, number=0):
        self.title = title
        self.project_webpage = project_webpage
        self.number = number

    def logic(self):
        links = self.collect_links()
        chapters = {}
        for link in links:
            text = self.collect_chapter(link)
            chapter = {self.number: link + text}
            self.number += 1
            chapters.update(chapter)

        write(self.title, chapters, "zh")

    def collect_chapter(self, url):
        page = self.get_webpage(url)
        text = page.find("div", class_="article fix").text
        return text

    def collect_links(self):
        page = self.get_webpage(self.project_webpage)

        raw_links = [link.get('href') for link in page.find_all("a")
                     if re.match(r'/read/\d+/\d+', link.get('href'))]
        write(self.title, {i: link for i, link in enumerate(raw_links)}, "zh")
        return raw_links

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
