import asyncio
import random
import re
import aiohttp
from bs4 import BeautifulSoup
from domain.file_tools import write
from parser.abstract_strategy import ParserStrategy


class XiaoShuo(ParserStrategy):
    def __init__(self, title, project_webpage):
        self.title = title
        self.project_webpage = project_webpage

    async def logic(self):
        links = await self.collect_links()
        await write(self.title, links, "zh")
        chapters = {}
        for chapter, link in links.items():
            await asyncio.sleep(random.randint(10, 30))
            text = await self.collect_chapter(link.strip())
            match = re.search(r'\d+', chapter)
            chapter = {match.group(0):
                       chapter + "/n" + link + text}
            chapters.update(chapter)

        await write(self.title, chapters, "zh")

    async def collect_chapter(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.encoding = response.apparent_encoding
                page = BeautifulSoup(await response.text(), 'html.parser')
                text = page.find("div", id="content").text
                return text

    async def collect_links(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.project_webpage) as response:
                response_text = await response.text()
                page = BeautifulSoup(response_text, 'html.parser')
                links = {link.text:
                         'https://www.147xiaoshuo.com/' + link.get("href")
                         for link in page.find('div', id='list').find_all("a")}
                return links

    def get_next_link(self):
        pass

    def check(self):
        pass
