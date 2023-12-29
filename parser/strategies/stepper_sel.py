import asyncio
import random
import re
from bs4 import BeautifulSoup
from loguru import logger
from domain.file_tools import read, write
from parser.abstract_strategy import ParserStrategy
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class StepperSel(ParserStrategy):

    def __init__(self, title, webpage, number):
        self.title = title
        self.webpage = webpage
        self.library = {}
        self.number = number
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
                page, next_link = await self.getter.get_webpage(url)
                text = self.collect_chapter(page, tag_sets[0]["tag"],
                                            tag_sets[0]["extra_tag"])
                chapter = {self.number: url + text}
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


class WebPageGetter:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        self.browser = webdriver.Chrome(options=options, service=service)

    async def get_webpage(self, url):
        self.browser.get(url)
        self.browser.maximize_window()
        try:
            next_button = self.browser.find_elements(
                By.CLASS_NAME, 'wp-block-button__link')[2]
            next_button.location_once_scrolled_into_view
            self.browser.execute_script("arguments[0].click()", next_button)
            # next_button = WebDriverWait(self.browser, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//div[@class='wp-block-button']/a[text()='NEXT']")))
            # self.browser.execute_script("arguments[0].scrollIntoView();",
            #                             next_button)
            # await asyncio.sleep(random.randint(15, 120))
            # next_button.click()
            next_link = self.browser.current_url
        except Exception as e:
            logger.error(e)
            next_link = None
        html = self.browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        return soup, next_link
