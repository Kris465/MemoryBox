from bs4 import BeautifulSoup
import requests
import re
from db import get_session
from models import Parser


class Parser_:

    def __init__(self, URL):
        self.__headers = {'User-Agent':
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                           AppleWebKit/537.36 (KHTML, like Gecko)\
                           Chrome/111.0.0.0 Safari/537.36'}
        self.__url = URL
        self.__tag = 'div'
        self.__cl = 'entry-content'

    @property
    def headers(self):
        return self.__headers

    @headers.setter
    def headers(self, headers):
        self.__headers = headers

    @property
    def tag(self):
        return self.__tag

    @property
    def cl(self):
        return self.__cl

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, URL):
        self.__url = URL

    def check_tags(self):
        print("Checking tags...")
        temp_url = re.sub(r'^https?://(?:www\.)?(.*?)/.*$',
                          r'\1',
                          self.__url)
        print(temp_url)
        session = get_session()
        result = session.query(Parser).filter(Parser.url == temp_url).all()
        if len(result) == 1:
            for webpage in result:
                self.__tag = webpage.tag
                self.__cl = webpage.cl
                print(self.tag, self.cl)
        elif len(result) == 0:
            self.__tag = input("tag: ")
            self.__cl = input("class: ")
            new_webpage = Parser(url=temp_url,
                                 tag=self.__tag,
                                 cl=self.__cl)
            session.add(new_webpage)
            session.commit()
        else:
            print("Check datebase!!!")

    def parse(self):
        page = requests.get(self.__url, headers=self.headers)
        print(page.status_code)
        soup = BeautifulSoup(page.text, "lxml")
        text = soup.find_all(self.tag, self.cl)
        return text

    def find_button(self):
        url = self.__url
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            if 'next' in link.text.lower():
                next_url = link['href']
                print(next_url)
                break
            else:
                next_url = None
        return next_url
