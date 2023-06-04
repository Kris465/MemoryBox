import random
import time
from bs4 import BeautifulSoup
import requests
import re
from chapter_class import Chapter
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

    def connection(self, language, urls=False):
        response = requests.get(self.url, headers=self.headers)
        print(response.status_code)
        if language == "chi":
            response.encoding = response.apparent_encoding
            time.sleep(random.randint(10, 120))
            soup = BeautifulSoup(response.text, 'html.parser')
            if urls:
                links = soup.find_all('a')
                return links
            else:
                text = soup.find_all(self.tag, self.cl)
                return text
        else:
            soup = BeautifulSoup(response.text, "lxml")
            if urls:
                links = soup.find_all('a')
                return links
            else:
                text = soup.find_all(self.tag, self.cl)
                return text

    def parse(self, mod, language):
        chapters = []
        match mod:
            case "stepper":
                link = self.url
                while link is not None:
                    time.sleep(10)
                    if link[0] != "h":
                        self.url = 'https:/' + link
                    else:
                        self.url = link

                    self.check_tags()
                    result = self.connection(language)
                    chapter = Chapter(self.chapter,
                                      self.url,
                                      str([i.text for i in result]))
                    chapters.append(chapter)
                    links = self.connection(language, urls=True)
                    for link in links:
                        if self.word.upper() in link.text.upper():
                            link = link['href']
                            break
                        else:
                            link = None
                return chapters
            case "collector":
                path = re.sub(r'^https?://[^/]+', '', self.url)
                time.sleep(random.randint(10, 120))
                links = self.connection(language, urls=True)
                new_links = []
                for link in links:
                    href = link.get('href')
                    if href and href.startswith(path):
                        new_links.append(href)

                sorted_links = sorted(set(new_links))
                for link in sorted_links:
                    print(link, sorted_links.index(link))
                    time.sleep(random.randint(20, 120))
                    text = self.connection(language)
                    print(text)
                    chapter = Chapter(sorted_links.index(link) + 1,
                                      link,
                                      text)
                    chapters.append(chapter)
                return chapters
        return None
