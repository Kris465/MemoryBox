import requests
from time import sleep
from random import randint
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from loguru import logger

from tools.file_manager import read_from_json
from tools.other_tools import get_domain_name


class Checker:
    def __init__(self, link):
        self.link = link
        self.name = get_domain_name(self.link)
        self.result = False
        self.tool = ""
        self.session = requests.Session()
        self.playwright_context = None

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

    def get_page_with_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        response = self.session.get(self.link, headers=headers)
        response.encoding = response.apparent_encoding

        if response.status_code != 200:
            logger.error(f"Ошибка {response.status_code} при запросе {self.link}")
            return None

        return response.text

    def get_page_with_playwright(self):
        try:
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch()
                context = browser.new_context()
                page = context.new_page()
                page.goto(self.link)
                page.wait_for_selector(self.selector)

                html = page.content()
                context.close()
                browser.close()
                return html
        except Exception as e:
            logger.error(f"Ошибка при работе Playwright: {e}")
            return None

    def parse_html(self, html):
        if not html:
            return None

        page = BeautifulSoup(html, 'html.parser')
        link = page.select_one(self.selector)

        if not link:
            logger.error(f"Не удалось найти элемент по селектору: {self.selector}")
            return None

        extracted_link = link.select_one("a")['href']
        logger.info(f"Извлеченная ссылка: {extracted_link}")
        return extracted_link

    def check_link_validity(self, extracted_link):
        if not extracted_link:
            return False

        sleep(randint(7, 20))  # Анти-бот задержка

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': self.link
            }

            response = self.session.get(extracted_link, headers=headers)
            logger.info(f"Статус код проверки ссылки: {response.status_code}")

            if response.status_code == 200:
                self.link = extracted_link
                return True
            else:
                logger.error(f"Ошибка {response.status_code} при запросе {extracted_link}")
                return False
        except Exception as e:
            logger.error(e)
            return False

    def parse(self):
        html = None

        match self.tool:
            case "requests":
                html = self.get_page_with_requests()
            case "playwright":
                html = self.get_page_with_playwright()
            case _:
                logger.error(f"Неизвестный инструмент: {self.tool}")
                self.result = False
                return

        extracted_link = self.parse_html(html)
        self.result = self.check_link_validity(extracted_link)
