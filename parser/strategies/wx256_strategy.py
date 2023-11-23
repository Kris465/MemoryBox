import re
import aiohttp
from bs4 import BeautifulSoup
from loguru import logger
from domain.file_tools import write
from parser.abstract_strategy import ParserStrategy


class Wx256(ParserStrategy):
    def __init__(self, title, project_webpage):
        self.title = title
        self.project_webpage = project_webpage
        self.number = 0

    async def logic(self):
        links = await self.collect_links()
        chapters = {}
        for link in links:
            text = await self.collect_chapter(link)
            chapter = {self.number: 'https://www.256wx.net' + link + text}
            self.number += 1
            chapters.update(chapter)

        await write(self.title, chapters, "zh")

    async def collect_chapter(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://www.256wx.net' + url) as response:
                page = BeautifulSoup(await response.text(), 'html.parser')
                text = page.find("div", class_="article fix").text
                logger.info(f"{self.number} / {url} / {text[30:]}")
                return text

    async def collect_links(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.project_webpage) as response:
                page = BeautifulSoup(await response.text(), 'html.parser')
                raw_links = [link.get('href') for link in page.find_all("a")
                             if re.match(r'/read/\d+/\d+', link.get('href'))]
                logger.info(f"links are collected / "
                            f"{raw_links[0]}...{raw_links[-1]}")
                return raw_links

    def get_next_link(self):
        pass

    def check(self):
        pass
