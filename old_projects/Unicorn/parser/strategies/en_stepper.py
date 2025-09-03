import asyncio
import random
import re
from bs4 import BeautifulSoup
from loguru import logger
import requests
from domain.file_tools import read, write
from parser.abstract_strategy import ParserStrategy


class EnStepper(ParserStrategy):
    def __init__(self, title, webpage, number):
        self.title = title
        self.webpage = webpage
        self.number = number
        self.library = {}

    async def logic(self):
        self.library = await read("library.json")
        url = self.webpage
        chapters = {}
        next_link = " "
        page = " "
        webpage_name = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1',
                              self.webpage)
        tag_sets = self.library[webpage_name]
        while next_link and page is not None:
            await asyncio.sleep(random.randint(5, 15))
            try:
                page = await asyncio.to_thread(self.get_webpage, url)
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
            except Exception as e:
                logger.error(e)
                break
        await write(self.title, chapters)

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
                if webpage_name in link["href"]:
                    next_link = link['href']
                else:
                    next_link = f"https://{webpage_name}/{link['href']}"
                    # next_link = f"https://{webpage_name}{link['href']}"
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
