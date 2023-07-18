import random
import time
from bs4 import BeautifulSoup
import requests
from parser.abstract_strategy import ParserStrategy


class ChiCollector(ParserStrategy):
    '''
    Chinese, collector, with checks for tags
    '''

    def __init__(self, title, project_webpage, number=0):
        self.title = title
        self.project_webpage = project_webpage
        self.number = number

    def logic(self):
        soup = self.get_webpage(self.project_webpage)

    def collect_chapter(self):
        pass

    def collect_links(self):
        pass

    def get_webpage(self, language='zh'):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
        time.sleep(random.randint(10, 120))
        response = requests.get(self.project_webpage, headers=headers)
        print(response.status_code)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def check(self):
        pass
