import requests
import playwright
from bs4 import BeautifulSoup
from loguru import logger

from tools.file_manager import read_from_json


class Checker:
    def __init__(self, link):
        self.link = link
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

        # selector =
        # button =
        # tool =

        logger.info("Отработал!")

    def logic(self):
        self.tool_box()
        self.parse()

    def parse(self):
        pass
