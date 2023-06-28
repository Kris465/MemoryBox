from bs4 import BeautifulSoup
import requests

from use_cases.parser.abstract_strategy import ParserStrategy


class Stepper(ParserStrategy):

    def __init__(self, chapters):
        self.chapters = chapters
        self.headers = {'User-Agent':
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/111.0.0.0 Safari/537.36'}

    def collect_chapters(self):
        

        number = 30
        all_chapters = []
        while number < 105:
            response = requests.get(url, headers=self.headers)
            print(response.status_code)
            soup = BeautifulSoup(response.text, 'lxml')
            result = soup.find_all("div", class_="entry-content")
            temp_dict = {number: url + i.text for i in result}
            print(temp_dict)
            all_chapters.update(temp_dict)
            soup = BeautifulSoup(response.text, "lxml")
            links = soup.find_all("a")
            for link in links:
                if "next" in link.text.lower():
                    next_link = link['href']
                    print(next_link)
                    break
                else:
                    next_link = None
            number += 1
            if next_link is None:
                url = input("url: ")
                if url == '':
                    break
            else:
                url = next_link

        return all_chapters
