import requests
from bs4 import BeautifulSoup
from domain.chapter_class import Chapter
from use_cases.parser.abstract_strategy import ParserStrategy


class Stepper(ParserStrategy):
    def __init__(self, cl, chapters=[]):
        self.cl = cl
        self.chapters = chapters

    def collect_chapters(self):
        # Проверяем, есть ли уже главы в списке
        if not self.chapters:
            ordinal_number = input("Введите номер первой главы: ")
            link = input("Введите ссылку на первую главу: ")
            chapter = self._parse_chapter(ordinal_number, link)
            self.chapters.append(chapter)

        # Ищем ссылку на следующую главу и продолжаем собирать главы
        while True:
            next_link = self._find_next_link(self.chapters[-1].link)
            if next_link is None:
                break
            chapter = self._parse_chapter(len(self.chapters) + 1, next_link)
            self.chapters.append(chapter)

        return self.chapters

    def _find_next_link(self, current_link):
        response = requests.get(current_link)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Ищем ссылку на следующую главу
        next_link = None
        for a_tag in soup.find_all('a'):
            if 'Next' in a_tag.text:
                next_link = a_tag.get('href')
                break

        return next_link

    def _parse_chapter(self, ordinal_number, link):
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'lxml')

        # Ищем текст главы
        text = soup.find(self.cl).text

        # Создаем объект главы и возвращаем его
        chapter = Chapter(ordinal_number, link, self.cl, text)
        return chapter
