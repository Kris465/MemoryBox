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
            for link in links:
                if self.word.upper() in link.text.upper():
                    next_url = link['href']
                    return next_url
            return None
        else:
            text = soup.find_all(self.tag, self.cl)
            return text

    # def parse(self, return_url=False):
    #     page = requests.get(self.__url, headers=self.headers)
    #     print(page.status_code)
    #     soup = BeautifulSoup(page.text, "lxml")
    #     if return_url:
    #         links = soup.find_all('a')
    #         self.__chapter = int(self.__url.split('-')[-1].replace('/', ''))
    #         for link in links:
    #             if self.word in link.text:
    #                 match = re.search(r'/(\d+(\.\d+)*)/', link['href'])
    #                 if match:
    #                     next_chapter = float(match.group(1))
    #                     if next_chapter >= self.__chapter + 1:
    #                         next_url = link['href']
    #                         return next_url
    #         return None
    #     else:
    #         text = soup.find_all(self.tag, self.cl)
    #         return text

    # def parse(self, return_url=False):
    #     page = requests.get(self.__url, headers=self.headers)
    #     print(page.status_code)
    #     soup = BeautifulSoup(page.text, "lxml")
    #     if return_url:
    #         links = soup.find_all('a')
    #         if self.word == 'Chapter':
    #             current_chapter = float(self.__url.split('-')[-1].replace('/', ''))
    #             for link in links:
    #                 if 'Chapter'.upper() in link.text.upper():
    #                     next_chapter = float(link['href'].split('-')[-1].replace('/', ''))
    #                     if next_chapter > current_chapter:
    #                         if next_chapter - current_chapter > 1:
    #                             print("Possible skipped chapters!")
    #                         next_url = link['href']
    #                         return next_url
    #                     else:
    #                         current_chapter += 0.1
    #             print("No more chapters!")
    #             return None
    #         elif self.word == 'Next':
    #             for link in links:
    #                 if 'Next'.upper() in link.text.upper():
    #                     next_url = link['href']
    #                     if len(next_url) - len(self.__url) > 5:
    #                         user_input = input("Is this the correct link? (Y/N)")
    #                         if user_input.upper() == 'Y':
    #                             return next_url
    #                         else:
    #                             user_url = input("Please enter the correct link:")
    #                             return user_url
    #                     else:
    #                         return next_url
    #             print("No 'Next' link found!")
    #             return None
    #         elif self.word == '下一章':
    #             for link in links:
    #                 if '下一章'.upper() in link.text.upper():
    #                     next_url = link['href']
    #                     return next_url
    #             print("No '下一章' link found!")
    #             return None
    #         else:
    #             for link in links:
    #                 if self.word.upper() in link.text.upper():
    #                     next_url = link['href']
    #                     return next_url
    #             print("No links found with the word '{}'!".format(self.word))
    #             return None
    #     else:
    #         text = soup.find_all(self.tag, self.cl)
    #         return text
