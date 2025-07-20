import requests
import playwright
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from loguru import logger

from tools.file_manager import read_from_json, update_json_file
from tools.other_tools import get_domain_name


class Checker:
    def __init__(self, link):
        self.link = link
        self.name = get_domain_name(self.link)
        self.result = False
        self.tool = ""

    def tool_box(self):
        '''
        Чтение конфига из selectors.json

        Структура json:
        {"доменное имя":{
            selector: значение селектора,
            button: текст кнопки,
            tool: playwright / requests
        }}

        '''
        data = read_from_json("selectors.json")
        self.tool = data[self.name]["tool"]
        self.selector = data[self.name]['selector']
        logger.info(f"Инструмент для новелы: {self.link} выбран: {self.tool}")

    def logic(self):
        self.tool_box()
        self.parse()

    def parse(self):
        match self.tool:
            case "requests":
                self.result = self.parsing_with_requests()
            case "playwright":
                self.result = self.parsing_with_playwright()
            case _:
                self.result = False

    def parsing_with_requests(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
        }

        response = requests.get(self.link, headers=headers)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            page = BeautifulSoup(response.text, 'html.parser')
            link = page.select_one(self.selector)
            extructed_link = link.select_one("a")['href']
            try:
                response = requests.get(extructed_link, 'html.parser')
                if response.status_code == 200:
                    self.result = True
                    update_novels_file(self.name, extructed_link)
            except Exception as e:
                logger.error(e)

    def parsing_with_playwright(self):
        pass
