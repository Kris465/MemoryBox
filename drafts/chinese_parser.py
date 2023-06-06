import random
import re
import time
from bs4 import BeautifulSoup
import requests
from parser_class import Parser_
from modules.writer_to_json import write


class Chinese(Parser_):

    def __init__(self, URL):
        super().__init__(URL)
        self.__cl = 'content_read'
        self.__word = '下一章'
        self.__chapter = 1

    def parse_links(self):
        path = re.sub(r'^https?://[^/]+', '', self.__url)
        time.sleep(random.randint(10, 120))
        response = requests.get(self.__url, headers=self.__headers)
        print(response.status_code)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')

        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith(path):
                links.append(href)

        sorted_links = sorted(set(links))
        links_dict = {"chapter" + str(i):
                      link for i, link in enumerate(sorted_links)}

        write("links", links_dict)
        return links_dict

    def parse(self):
        links_dict = self.parse_links()

        for k, v in links_dict.items():
            time.sleep(random.randint(20, 120))
            response = requests.get('https://www.shubaow.net' + v,
                                    headers=self.__headers)
            print(response.status_code)
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'html.parser')
            chapter_text = soup.find('div', "content_read").text
            temp_dict = {k: chapter_text}
            print(temp_dict)
            return temp_dict
