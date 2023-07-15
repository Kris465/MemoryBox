from bs4 import BeautifulSoup
import requests

class Parser:
    def __init__(self, title, chapter, url) -> None:
        self.title = title
        self.chapter = chapter
        self.url = url

    # Разветлвление под коллектор и степпер, либо ссылка на следующую главу, либо сбор глав
    def links_operator(self, soup):
        pass

    def get_webpage(self, language="en"):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}      
        response = requests.get(self.url, headers=headers)
        print(response.status_code)
        match language:
            case "en":
                soup = BeautifulSoup(response.text, 'lxml')
            case "zh":
                response.encoding = response.apparent_encoding
                soup = BeautifulSoup(response.text, 'html.parser')
            case _:
                soup = None
        return soup