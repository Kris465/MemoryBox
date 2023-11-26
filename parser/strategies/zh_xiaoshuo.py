import asyncio
import random
from bs4 import BeautifulSoup

from loguru import logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from domain.file_tools import write
from parser.abstract_strategy import ParserStrategy


class XiaoShuo(ParserStrategy):
    def __init__(self, title, project_webpage):
        self.title = title
        self.project_webpage = project_webpage

    async def logic(self):
        getter = WebPageGetter()
        soup = await getter.get_webpage(self.project_webpage)
        links = await self.collect_links(soup)
        chapters = {}

        for chapter, link in links.items():
            temp_soup = None
            text = None
            while not text:
                try:
                    temp_soup = await getter.get_webpage(link.strip())
                    text = await self.collect_chapter(temp_soup)
                except Exception:
                    if self.browser:
                        self.browser.quit()
                        await asyncio.sleep(random.randint(10, 360))
                        self.browser = webdriver.Chrome()
                        self.browser.set_window_size(1920, 1080)

            chapter = {chapter: link + text}
            chapters.update(chapter)

        await write(self.title, chapters, "zh")

    async def collect_chapter(self, soup):
        chapter = soup.find("div", id="content").text
        logger.info(f"Text is collected {chapter[:10]}")
        return chapter

    async def collect_links(self, soup):
        raw_links = soup.find('div', id='list').find_all("a")
        number = 1
        links = {}
        for link in raw_links:
            href = link.get('href')
            try:
                links.update({number: "https://www.147xiaoshuo.com" + href})
                number += 1
            except AttributeError:
                continue
        logger.info(f"Links are collected: {links}")
        return links


class WebPageGetter:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        self.browser = webdriver.Chrome(options=options, service=service)

    async def get_webpage(self, url):
        self.browser.get(url)
        await asyncio.sleep(random.randint(15, 120))
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        return soup
