import asyncio
import random
import re
import aiohttp
from bs4 import BeautifulSoup
from parser.abstract_strategy import ParserStrategy
from write_to_json import write


class ChiShuka(ParserStrategy):
    def __init__(self, title, project_webpage):
        self.title = title
        self.project_webpage = project_webpage
        self.number = 0

    async def logic(self):
        soup = await self.get_webpage(self.project_webpage)
        links = await self.collect_links(soup)
        print(links)
        chapters = {}
        for k, v in links.items():
            print(k, v)
            text = await self.collect_chapter(v)
            chapter = {k: v + text}
            print(chapter)
            chapters.update(chapter)
        write(self.title, chapters, language="zh")

    async def collect_chapter(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                page = BeautifulSoup(await response.text(), 'html.parser')
                chapter = page.find("article", class_="article-content").text
                return chapter

    async def collect_links(self, soup):
        links = {}
        raw_links = soup.find(
            "article", class_="article-content").find_all("a")
        for link in raw_links:
            href = link.get('href')
            try:
                number = re.search(r'(\d+)\.html', href).group(1)
                links.update({int(number) - 1: href})
            except AttributeError:
                continue

        return links

    async def get_webpage(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
        await asyncio.sleep(random.randint(10, 40))
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                page = BeautifulSoup(await response.text(), 'html.parser')
                return page
