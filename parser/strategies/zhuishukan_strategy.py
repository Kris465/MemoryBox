import random
import time
from bs4 import BeautifulSoup
import requests
from parser.abstract_strategy import ParserStrategy
from write_to_json import write


class Zhuishukan(ParserStrategy):
    def __init__(self, title, project_webpage, number=0):
        self.title = title
        self.project_webpage = project_webpage
        self.number = number

    def logic(self):
        links = self.collect_links()
        chapters = {}
        # Переписать магические переменные. Регулярка для адреса ниже"
        for k, v in links.items():
            url = "https://m.zhuishukan.com" + v
            text = ""
            while url is not None:
                soup = self.get_webpage(url)
                text += self.collect_chapter(soup)
                next_link = self.get_next_link(soup)
                url = next_link
            temp_dict = {k: text}
            chapters.update(temp_dict)
        write(self.title, chapters, language="zh")

    def collect_chapter(self, soup):
        print(soup.text)
        chapter = soup.find("div", class_="content")
        return chapter.text

    def collect_links(self):
        url = self.project_webpage
        soup = ""
        links = []
        while url is not None:
            soup = self.get_webpage(url)
            links_pack = soup.find("ul", class_="read").find_all("a")
            for link in links_pack:
                href = link.get("href")
                links.append(href)
            url = self.get_next_link(soup)

        sorted_links = sorted(links)
        links = {str(i): link for i, link in enumerate(sorted_links)}
        return links

    def get_webpage(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
        time.sleep(random.randint(10, 40))
        response = requests.get(url, headers=headers)
        print(response.status_code)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def check(self):
        # Дописать метод сверки по тегам
        pass

    def get_next_link(self, soup):
        links = soup.find_all("a")
        for link in links:
            if "下一页" in link.text:
                next_link = "https://m.zhuishukan.com" + link['href']
                return next_link
            else:
                next_link = None
        return next_link
