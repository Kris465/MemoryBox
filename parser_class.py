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
        self.__word = 'next'
        self.__chapter = 1
        self.previous_url = ' '

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

    @property
    def word(self):
        return self.__word

    @property
    def chapter(self):
        return self.__chapter

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
                self.__word = webpage.word
                print(self.tag, self.cl, self.word)
        elif len(result) == 0:
            self.__tag = input("tag: ")
            self.__cl = input("class: ")
            self.__word = input("word: ")
            new_webpage = Parser(url=temp_url,
                                 tag=self.__tag,
                                 cl=self.__cl,
                                 word=self.__word)
            session.add(new_webpage)
            session.commit()
        else:
            print("Check datebase!!!")

    def parse(self, return_url=False):
        page = requests.get(self.__url, headers=self.headers)
        print(page.status_code)
        soup = BeautifulSoup(page.text, "lxml")
        if return_url:
            links = soup.find_all('a')
            return self.find_link(links)
        else:
            text = soup.find_all(self.tag, self.cl)
            return text

    def find_link(self, links):
        regex = r'[-/](\d+(\.\d+)*)/'
        for link in links:
            if self.word.upper() in link.text.upper():
                next_url = link['href']
                if next_url == self.previous_url:
                    continue
                self.previous_url = self.__url
                self.__chapter = re.findall(regex, next_url)[-1][0]
                return next_url
            else:
                user_input = input("Link: \n")
                if user_input == '':
                    return None
                else:
                    next_url = user_input
                    self.previous_url = self.__url
                    self.__chapter = re.findall(regex, next_url)[-1][0]
                    return next_url
        return None
