import asyncio
from bs4 import BeautifulSoup
from loguru import logger
import requests
from parser.abstract_strategy import ParserStrategy
from reader import read
from write_to_json import write


class Wfxs(ParserStrategy):
    '''
    Посмотреть как работает эта стратегия! Видоизменить,
    чтобы работал китайский степпер.
    '''

    def __init__(self, title, project_webpage):
        self.title = title
        self.project_webpage = project_webpage
        self.number = 0
        self.library = read("library.json")

    async def logic(self):
        soup = await asyncio.to_thread(self.get_webpage, self.project_webpage)
        links = self.collect_links(soup)
        chapters = {}
        for k, v in links.items():
            url = "https://www.wfxs.com.tw" + v
            text = ""
            while url is not None:
                soup = await asyncio.to_thread(self.get_webpage, url)
                text += self.collect_chapter(soup)
                next_link = self.get_next_link(soup)
                url = next_link
            temp_dict = {k: text}
            chapters.update(temp_dict)
        write(self.title, chapters, language="zh")

    def collect_chapter(self, soup):
        chapter = soup.find("div", class_="readcontent")
        return chapter.text

    def collect_links(self, soup):
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith("/chapter"):
                links.append(href)

        sorted_links = sorted(set(links))
        links = {str(i): link for i, link in enumerate(sorted_links)}
        return links

    def get_webpage(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        logger.info(f"{self.title} / {url} / {response.status_code}")
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def check(self):
        pass

    def get_next_link(self, soup):
        links = soup.find_all("a")
        for link in links:
            if "下一頁" in link.text:
                next_link = "https://www.wfxs.com.tw" + link['href']
                return next_link
        return None

# class Wfxs(ParserStrategy):
#     def __init__(self, title, project_webpage):
#         self.title = title
#         self.project_webpage = project_webpage
#         self.number = 0

#     def logic(self):
#         soup = self.get_webpage(self.project_webpage)
#         links = self.collect_links(soup)
#         chapters = {}
#         # Переписать магические переменные. Регулярка для адреса ниже"
#         for k, v in links.items():
#             url = "https://www.wfxs.com.tw" + v
#             text = ""
#             while url is not None:
#                 soup = self.get_webpage(url)
#                 text += self.collect_chapter(soup)
#                 next_link = self.get_next_link(soup)
#                 url = next_link
#             temp_dict = {k: text}
#             chapters.update(temp_dict)
#         write(self.title, chapters, language="zh")

#     def collect_chapter(self, soup):
#         chapter = soup.find("div", class_="readcontent")
#         return chapter.text

#     def collect_links(self, soup):
#         links = []
#         for link in soup.find_all('a'):
#             href = link.get('href')
#             if href and href.startswith("/chapter"):
#                 links.append(href)

#         sorted_links = sorted(set(links))
#         links = {str(i): link for i, link in enumerate(sorted_links)}
#         return links

#     def get_webpage(self, url):
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
#                                 AppleWebKit/537.36 (KHTML, like Gecko)\
#                                 Chrome/111.0.0.0 Safari/537.36'}
#         time.sleep(random.randint(10, 40))
#         response = requests.get(url, headers=headers)
#         print(response.status_code)
#         response.encoding = response.apparent_encoding
#         soup = BeautifulSoup(response.text, 'html.parser')
#         return soup

#     def check(self):
#         # Дописать метод сверки по тегам
#         pass

#     def get_next_link(self, soup):
#         links = soup.find_all("a")
#         for link in links:
#             if "下一頁" in link.text:
#                 next_link = "https://www.wfxs.com.tw" + link['href']
#                 return next_link
#             else:
#                 next_link = None
#         return next_link
