import asyncio
import random
import re
import aiohttp
from bs4 import BeautifulSoup
from loguru import logger
from domain.file_tools import write
from parser.abstract_strategy import ParserStrategy


class ChiShuka(ParserStrategy):
    def __init__(self, title, project_webpage):
        self.title = title
        self.project_webpage = project_webpage
        self.number = 0

    async def logic(self):
        soup = await self.get_webpage(self.project_webpage)
        links = await self.collect_links(soup)
        chapters = {}
        for k, v in links.items():
            temp_soup = await self.get_webpage(v)
            try:
                text = await self.collect_chapter(temp_soup)
            except Exception as e:
                logger.error(f"Couldn't collect chapter {k} in {self.title}"
                             f"{e}")
            chapter = {k: v + text}
            chapters.update(chapter)
            logger.info(f"{k} / {v} / {self.title}")
        await write(self.title, chapters, language="zh")

    async def collect_chapter(self, soup):
        try:
            chapter = soup.find("article", class_="article-content").text
            logger.info(f"{chapter[:10]}")
        except AttributeError:
            chapter = " "
            logger.error("Page doesn't have text")
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

        logger.info(f"{links}")
        return links

    async def get_webpage(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                            AppleWebKit/537.36 (KHTML, like Gecko)\
                            Chrome/111.0.0.0 Safari/537.36'}
        await asyncio.sleep(random.randint(5, 15))
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    page = await response.text()
                    encoding = response.charset or 'utf-8'
                    soup = BeautifulSoup(page, 'html.parser',
                                         from_encoding=encoding)
        except Exception as e:
            logger.error(f"Shuka / {url} / couldn't collect / {e}")
            soup = None

        return soup
