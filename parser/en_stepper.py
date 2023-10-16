from bs4 import BeautifulSoup
import requests
from parser.abstract_strategy import ParserStrategy
from write_to_json import write


class EnStepper(ParserStrategy):
    def __init__(self, title, webpage):
        self.title = title
        self.webpage = webpage
        self.tag = "div"
        self.extra_tag = "entry-content"
        self.word = "next"
        self.number = 1

    def logic(self):
        url = self.webpage
        chapters = {}
        next_link = " "
        self.number = input("chapter: ")
        while next_link is not None:
            chapter = self.collect_chapter(url)
            next_link = self.get_next_link(url)
            chapters.update(chapter)
            self.number += 1
        write(self.title, chapters)

    def collect_chapter(self, url):
        page = self.get_webpage(url)
        text = page.find(self.tag).find_all(self.extra_tag)
        return {self.number: url + text}

    def collect_links(self):
        pass

    def get_next_link(self, url):
        #собрать ссылку на следующую страницу
        pass

    def get_webpage(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def check(self):
        pass
