import asyncio
import random
import re
from bs4 import BeautifulSoup

from loguru import logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from domain.file_tools import read, write
from parser.abstract_strategy import ParserStrategy


class EnCollector(ParserStrategy):
    def __init__(self, title, project_webpage):
        self.title = title
        self.project_webpage = project_webpage
        self.library = {}

    async def logic(self):
        self.library = await read("library")
        webpage_name = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1',
                              self.project_webpage)
        tag_sets = self.check(webpage_name)

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
                    text = await self.collect_chapter(temp_soup,
                                                      tag_sets[0]["tag"],
                                                      tag_sets[0]["extra_tag"])
                except Exception:
                    if self.browser:
                        self.browser.quit()
                        await asyncio.sleep(random.randint(10, 360))
                        self.browser = webdriver.Chrome()
                        self.browser.set_window_size(1920, 1080)

            chapter = {chapter: f"{link} \n {text}"}
            chapters.update(chapter)

        await write(self.title, chapters)

    async def collect_chapter(self, soup, tag, extra_tag):
        try:
            chapter = soup.find(tag, class_=extra_tag).text
        except Exception:
            chapter = soup.find(tag, id=extra_tag).text
            logger.info("id for extra-tag")

        logger.info(f"Text is collected {chapter[:10]}")
        return chapter

    async def collect_links(self, soup):
        raw_links = soup.find_all("a")
        number = 1
        links = {}
        for link in raw_links:
            try:
                href = link.get('href')
                links.update({number: href})
                number += 1
            except ArithmeticError:
                continue
        logger.info(f"Links are collected: {links}")
        return links

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


class WebPageGetter:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('-ignore-certificate-errors')
        self.browser = webdriver.Chrome(service=service,
                                        options=chrome_options)

    async def get_webpage(self, url):
        self.browser.get(url)
        await asyncio.sleep(random.randint(5, 20))
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        logger.info("Soup is created! Selenium.")
        return soup
