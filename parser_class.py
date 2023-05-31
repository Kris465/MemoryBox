import random
import time
from bs4 import BeautifulSoup
import requests
import re
from db_session import get_session
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

    @chapter.setter
    def chapter(self, chapter):
        self.__chapter = chapter

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

    # def parse(self, mod, language, return_url=False):
    #     page = requests.get(self.__url, headers=self.__headers)
    #     print(page.status_code)
    #     soup = BeautifulSoup(page.text, "lxml")

    #     match mod:
    #         case "stepper":
    #             if return_url:
    #                 next_url = self.get_next_url(soup)
    #                 return next_url
    #             else:
    #                 text = self.get_chapter_text(soup, language)
    #                 return text
    #         case "collector":
    #             links_dict = self.get_all_links(soup)
    #             for k, v in links_dict.items():
    #                 time.sleep(random.randint(20, 120))
    #                 pass

    # def get_next_url(self, soup):
    #     links = soup.find_all('a')
    #     for link in links:
    #         if self.word.upper() in link.text.upper():
    #             next_url = link['href']
    #             print(next_url)
    #             return next_url
    #     return None

    # def get_chapter_text(self, soup, language):
    #     if language == "chi":
    #         text = soup.find('div', class_='content_read').text
    #     else:
    #         text = soup.find_all(self.tag, self.cl)
    #         text = [t.text for t in text]
    #         text = "\n".join(text)
    #     return text

    # def get_all_links(self, soup):
    #     links_dict = {}
    #     links = soup.find_all('a')
    #     for link in links:
    #         if "chapter" in link['href']:
    #             chapter_number = link.text.split()[1]
    #             links_dict[chapter_number] = link['href']
    #     return links_dict
    
    # def parse(self, return_url=False):
    #     page = requests.get(self.__url, headers=self.headers)
    #     print(page.status_code)
    #     soup = BeautifulSoup(page.text, "lxml")
    #     if return_url:
    #         links = soup.find_all('a')
    #         for link in links:
    #             if self.word.upper() in link.text.upper():
    #                 next_url = link['href']
    #                 print(next_url)
    #                 break
    #             else:
    #                 next_url = None
    #         return next_url
    #     else:
    #         text = soup.find_all(self.tag, self.cl)
    #         return text

    def connection(self, language):
        response = requests.get(self.__url, headers=self.__headers)
        print(response.status_code)
        if language == "chi":  
            response.encoding = response.apparent_encoding
            time.sleep(random.randint(10, 120))
            soup = BeautifulSoup(response.text, 'html.parser')
        else:
            soup = BeautifulSoup(response.text, "lxml")
        return soup

    def parse(self, mod, language):
        objects = []
