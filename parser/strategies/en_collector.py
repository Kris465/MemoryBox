import asyncio
import random
import aiohttp
from bs4 import BeautifulSoup
from loguru import logger
from parser.abstract_strategy import ParserStrategy
from write_to_json import write


class EnCollector(ParserStrategy):
    def __init__(self, title, webpage) -> None:
        self.title = title
        self.webpage = webpage

    async def logic(self):
        soup = await self.get_webpage(self.project_webpage)
        links = await self.collect_links(soup)
        logger.info(f"links: {links[0]} ... {links[-1]}")
        chapters = {}
        for k, v in links.items():
            text = await self.collect_chapter(v)
            chapter = {k: v + text}
            chapters.update(chapter)
        write(self.title, chapters, language="zh")

    async def collect_chapter(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                page = BeautifulSoup(await response.text(), 'html.parser')
                chapter = page.find("article", class_="article-content").text
                logger.info(f"text is collected {chapter[30:]}")
                return chapter

    async def collect_links(self, soup):
        links = {}
        raw_links = soup.find(
            "entry-content").find_all("a")
        for link in raw_links:
            if "Continue reading " in link.text:
                href = link.get('href')
                links.update({link.find('span').text: href})
            else:
                continue

        logger.info(f"{links}")
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
