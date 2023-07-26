# import random
# import time
from bs4 import BeautifulSoup

import requests
from parser.abstract_strategy import ParserStrategy
from write_to_json import write


class Ranwen(ParserStrategy):

    def __init__(self, title, project_webpage, number=0):
        self.title = title
        self.project_webpage = project_webpage
        self.number = number

    def logic(self):
        links = self.collect_links()
        number = self.number
        all_chapters = {}
        for link in links:
            soup = self.get_webpage(link)
            text = self.collect_chapter(soup)
            temp_dict = {number: text}
            all_chapters.update(temp_dict)
            number += 1
        write(self.title, all_chapters)

    def get_webpage(self, url):
        headers = {"Scheme": "https",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                   "Accept-Encoding": "gzip, deflate, br",
                   "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                   "Cache-Control": "max-age=0",
                   "Cookie": "__51vcke__JPU7oCFPtGBMBVep=0ab59e03-729b-536d-8779-abeece604e90; __51vuft__JPU7oCFPtGBMBVep=1689714894450; cf_clearance=rmYRqgSss0eQ2pY0DHaK63MwJMMzfK5lO1Akwnuqf6c-1690209204-0-0.2.1690209204; __51cke__=; __51uvsct__JPU7oCFPtGBMBVep=7; __tins__21178631=%7B%22sid%22%3A%201690395768973%2C%20%22vd%22%3A%205%2C%20%22expires%22%3A%201690399292054%7D; __51laig__=9; __vtins__JPU7oCFPtGBMBVep=%7B%22sid%22%3A%20%2285565a28-1202-5f5d-9733-90118d8a504f%22%2C%20%22vd%22%3A%206%2C%20%22stt%22%3A%202529488%2C%20%22dr%22%3A%20806488%2C%20%22expires%22%3A%201690400098561%2C%20%22ct%22%3A%201690398298561%7D",
                   "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                   "Sec-Ch-Ua-Mobile": "?0",
                   "Sec-Ch-Ua-Platform": '"Windows"',
                   "Sec-Fetch-Dest": "document",
                   "Sec-Fetch-Mode": "navigate",
                   "Sec-Fetch-Site": "cross-site",
                   "Sec-Fetch-User": "?1",
                   "Upgrade-Insecure-Requests": "1",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
        # time.sleep(random.randint(10, 40))
        response = requests.get(url, headers=headers)
        print(response.status_code)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def collect_chapter(self, soup):
        text = soup.find("div", id="content")
        return text

    def collect_links(self):
        soup = self.get_webpage(self.project_webpage)
        links = soup.find("div", id="list").find_all("a")
        all_links = []
        for link in links:
            href = link.get('href')
            all_links.append(href)

        sorted_links = sorted(set(all_links))
        links = {str(i): link for i, link in enumerate(sorted_links)}
        return links
