from bs4 import BeautifulSoup
from loguru import logger
import requests
from write_to_json import write


class ParserStrategy():
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

    async def collect_chapter(self):
        pass

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
