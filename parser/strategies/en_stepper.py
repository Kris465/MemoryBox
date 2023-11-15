import asyncio
import re
from bs4 import BeautifulSoup
from loguru import logger
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

    async def logic(self):
        url = self.webpage
        chapters = {}
        next_link = " "
        page = " "
        self.number = int(input("chapter: "))
        webpage_name = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1',
                              self.webpage)
        tag_sets = self.check(webpage_name)
        while next_link and page is not None:
            page = await asyncio.to_thread(self.get_webpage, url)
            try:
                text = self.collect_chapter(page, tag_sets[0]["tag"],
                                            tag_sets[0]["extra_tag"])
                chapter = {self.number: url + text}
                next_link = self.get_next_link(page, tag_sets[0]["word"],
                                               webpage_name)
                if next_link == url:
                    break
                logger.info(f"text is collected - {self.number} - {next_link}")
                chapters.update(chapter)
                self.number += 1
                url = next_link
            except AttributeError:
                logger.warning("AttributeError")
                break
        write(self.title, chapters)

    def collect_chapter(self, page, tag, extra_tag):
        try:
            result = page.find_all(tag, class_=extra_tag)
        except ValueError:
            result = page.find_all(tag, id=extra_tag)
            logger.info("id for extra-tag")
        text = "".join(set([i.text for i in result]))
        return text

    def collect_links(self):
        pass

    def get_next_link(self, page, word, webpage_name):
        links = page.find_all("a")
        for link in links:
            # if word in link.text:
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
        logger.info(f"{self.title} / {url} / {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            return soup
        else:
            return

    def check(self, webpage_name):
        try:
            tag_sets = self.library[webpage_name]
        except KeyError:
            temp_dict = {webpage_name: [{"tag": input("tag: "),
                                         "extra_tag": input("extra_tag: "),
                                         "word": input("word: ")},
                                        {"strategy": "EnStepper"}]}
            dictionary = self.library
            dictionary.update(temp_dict)
            write("library", dictionary)
            tag_sets = temp_dict[webpage_name]
        return tag_sets
