import logging
import re
from bs4 import BeautifulSoup
import requests
from parser.abstract_strategy import ParserStrategy
from reader import read
from write_to_json import write


class EnStepper(ParserStrategy):
    def __init__(self, title, webpage):
        self.title = title
        self.webpage = webpage
        self.tag = "div"
        self.extra_tag = "chapter-content"
        self.word = "next"
        self.number = 1
        self.library = read("library.json")

    def logic(self):
        url = self.webpage
        chapters = {}
        next_link = " "
        self.number = int(input("chapter: "))
        while next_link is not None:
            page = self.get_webpage(url)
            text = self.collect_chapter(page)
            chapter = {self.number: url + text}
            next_link = self.get_next_link(page)
            chapters.update(chapter)
            print(self.number)
            self.number += 1
            url = next_link
        write(self.title, chapters)

    def collect_chapter(self, page):
        text = "".join(page.find(self.tag).find_all(self.extra_tag))
        print(text)
        return text

    def collect_links(self):
        pass

    def get_next_link(self, page):
        links = page.find_all("a")
        for link in links:
            if "next" in link.text.lower() and link["href"] != "#":
                try:
                    next_link = "https://www.wuxiap.com/" + link['href']
                    logging.info(f"link: {next_link}")
                except Exception:
                    next_link = input("url: ")
                    logging.error(f"User inputs a link: {next_link}")
                break
            else:
                next_link = None
        return next_link

    def get_webpage(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def check(self):
        url = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1', self.webpage)
        try:
            tag_sets = self.library[url]
        except KeyError:
            tag_sets = {url: [{"tag": input("tag: "), "extra_tag": input("extra_tag: "), "word": input("word: ")}]}
            self.library.update(tag_sets)
        return tag_sets
