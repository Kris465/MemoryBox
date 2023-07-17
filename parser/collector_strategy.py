from bs4 import BeautifulSoup
import requests
from parser.abstract_strategy import ParserStrategy
from write_to_json import write


class Collector(ParserStrategy):
    '''
    Collector, English, Novelupdates, Basic logic without checks
    '''

    def __init__(self, title, project_webpage, number=0):
        self.project_webpage = project_webpage
        self.number = number
        self.title = title

    def logic(self):
        all_chapters = {}
        soup = self.get_webpage(self.project_webpage)
        # collect_links()
        result = soup.find_all("a", class_="chp-release")
        for link in result:
            # collect_chapter
            url = link["href"]
            # check(rul) - проверить теги(на случай блуждания по разным сайтам)
            new_soup = self.get_webpage("https:" + url)
            text = new_soup.find("div", class_="entry-content")
            temp_dict = {link["title"]: link["href"] + text.text}
            all_chapters.update(temp_dict)
        write(self.title, all_chapters, "en")

    def get_webpage(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                                AppleWebKit/537.36 (KHTML, like Gecko)\
                                Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def collect_chapter(self):
        return super().collect_chapter()

    def collect_links(self):
        return super().collect_links()

    def check(self):
        return super().check()

    def get_next_link(self):
        return super().get_next_link()
