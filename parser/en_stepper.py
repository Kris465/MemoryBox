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
        self.number = 1
        self.library = read("library.json")

    def logic(self):
        url = self.webpage
        chapters = {}
        next_link = " "
        self.number = int(input("chapter: "))
        webpage_name = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1',
                              self.webpage)
        tag_sets = self.check(webpage_name)
        while next_link is not None:
            page = self.get_webpage(url)
            text = self.collect_chapter(page, tag_sets[0]["tag"],
                                        tag_sets[0]["extra_tag"])
            chapter = {self.number: url + text}
            next_link = self.get_next_link(page, tag_sets[0]["word"],
                                           webpage_name)
            chapters.update(chapter)
            print(self.number)
            self.number += 1
            url = next_link
        write(self.title, chapters)

    def collect_chapter(self, page, tag, extra_tag):
        result = page.find_all(tag, class_=extra_tag)
        text = "".join([i.text for i in result])
        print(text)
        return text

    def collect_links(self):
        pass

    def get_next_link(self, page, word, webpage_name):
        links = page.find_all("a")
        for link in links:
            if word in link.text.lower() and link["href"] != "#":
                try:
                    if webpage_name in link["href"]:
                        next_link = link['href']
                    else:
                        next_link = f"https://{webpage_name}/{link['href']}"
                except Exception:
                    next_link = input("url: ")
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

    def check(self, webpage_name):
        try:
            tag_sets = self.library[webpage_name]
        except KeyError:
            temp_dict = {webpage_name: [{"tag": input("tag: "),
                                         "extra_tag": input("extra_tag: "),
                                         "word": input("word: ")}]}
            dictionary = self.library
            dictionary.update(temp_dict)
            write("library", dictionary)
            tag_sets = temp_dict[webpage_name]
        return tag_sets
