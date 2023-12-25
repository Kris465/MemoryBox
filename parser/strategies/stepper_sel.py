import asyncio
import random
import re
from bs4 import BeautifulSoup
from loguru import logger
from domain.file_tools import read, write
from parser.abstract_strategy import ParserStrategy
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class StepperSel(ParserStrategy):
    def __init__(self, title, webpage, number):
        self.title = title
        self.webpage = webpage
        self.number = number
        self.library = {}
        self.getter = WebPageGetter()

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
                page = await self.getter.get_webpage(url)
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
            if word in link.text:
                if webpage_name in link["href"]:
                    next_link = link['href']
                else:
                    next_link = f"https://{webpage_name}/{link['href']}"
                break
            else:
                next_link = None
        return next_link


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
