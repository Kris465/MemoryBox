import requests
from bs4 import BeautifulSoup
from loguru import logger


class Checker:
    def __init__(self, link):
        self.link = link
        self.result = False

    def parse(self):
        response = requests.get(self.link)
        if response.status_code == 200:
            logger.info("I'm in class Checker, method parse")
            page = BeautifulSoup(response.text, 'html.parser')
            res = page.find_all("a")
            logger.info(res)

            return [a.get('href', 'No href') for a in res[:10]]

        logger.warning(f"Ошибка запроса: {response.status_code}")
        return None
