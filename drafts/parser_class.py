from bs4 import BeautifulSoup
import requests


class Parser:

    def __init__(self, URL, tag, cl):
        self.__headers = {'User-Agent':
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                           AppleWebKit/537.36 (KHTML, like Gecko)\
                           Chrome/111.0.0.0 Safari/537.36'}
        self.__URL = URL
        self.__tag = tag
        self.__cl = cl

    @property
    def headers(self):
        return self.__headers

    @headers.setter
    def headers(self, headers):
        self.__headers = headers

    @property
    def URL(self):
        return self.__URL

    @URL.setter
    def URL(self, URL):
        self.__URL = URL

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    @property
    def cl(self):
        return self.__cl

    @cl.setter
    def cl(self, cl):
        self.__cl = cl

    def parse(self):
        page = requests.get(self.URL, headers=self.headers)
        print(page.status_code)
        soup = BeautifulSoup(page.text, "lxml")
        table = soup.find_all(str(self.tag), class_=str(self.cl))
        return table
