import re
from bs4 import BeautifulSoup
from loguru import logger
import requests
from domain.file_tools import read, write
from parser.abstract_strategy import ParserStrategy


class DIYStrategy(ParserStrategy):
    def __init__(self, title, number, links) -> None:
        self.title = title
        self.number = number
        self.links = links
        self.library = {}

    async def logic(self):
        self.library = await read("library")
        novel = {}

        for link in self.links:
            page = self.get_webpage(link)
            webpage_name = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1',
                                  link)
            tag_sets = self.library[webpage_name]
            text = self.collect_chapter(page, tag_sets[0]["tag"],
                                        tag_sets[0]["extra_tag"])
            chapter = {self.number: link + text}
            novel.update(chapter)
            self.number += 1

        await write(self.title, novel)

    async def collect_chapter(self, soup, tag, extra_tag):
        try:
            result = soup.find_all(tag, class_=extra_tag)
        except ValueError:
            result = soup.find_all(tag, id=extra_tag)
            logger.info("id for extra-tag")
        text = "".join(set([i.text for i in result]))
        return text

    async def collect_links(self):
        pass

    async def get_next_link(self):
        pass

    async def get_webpage(self, url):
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

    async def check(self):
        pass
