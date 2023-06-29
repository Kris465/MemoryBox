from bs4 import BeautifulSoup
import requests
from domain.chapter_class import Chapter

from use_cases.parser.abstract_strategy import ParserStrategy


class Stepper(ParserStrategy):

    def __init__(self, tag, cl, chapters):
        self.headers = {'User-Agent':
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/111.0.0.0 Safari/537.36'}
        self.tag = tag
        self.cl = cl
        self.chapters = chapters

    def collect_chapters(self):
        url = self.chapters[-1].link
        while url is not None:
            response = requests.get(url, headers=self.headers)
            print(response.status_code)
            soup = BeautifulSoup(response.text, 'lxml')
            links = soup.find_all("a")
            for link in links:
                if "next" in link.text.lower():
                    next_link = link["href"]
                    print(next_link)
                    break
                else:
                    next_link = None
            number = Chapter.ordinal_number + 1
            url = next_link
            result = soup.find_all(self.tag, class_=self.cl)

            # создание новой главы
            # присвоение главы в список глав
        
        return chapters
