import json
from writer_to_json import write
from reader_from_json import read
from parser_class import Parser
from translator import Translator
from writer_to_txt import write_txt


class Librarian():

    def __init__(self, title):
        self.__title = title
        self.__full_library = json.loads(open('librarian.json',
                                              encoding="UTF-8").read())
        self.__link = self.set_link(title)
        self.__chapters = self.set_chapters(title)

    @property
    def chapters(self):
        return self.__chapters

    def set_chapters(self, title):
        try:
            chapters = read(title)
        except Exception:
            chapters = None
            print("Глав нет")

        return chapters

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def link(self):
        return self.__link

    def set_link(self, title):
        link = self.__full_library.get(title)

        if link is None:
            link = input("Link? \n")
        else:
            link = link.get("url")

        return link

    @property
    def full_library(self):
        return self.__full_library

    @full_library.setter
    def full_library(self, full_library):
        self.__full_library = full_library

    def check_title(self):
        number = 1
        pages = int(input("Pages: \n"))
        links = {}
        if pages == 0:
            pars = Parser(self.__link, "a", "chp-release")
            result = pars.parse()
            links = {i['title']: i['href'] for i in result}
        else:
            URL = self.__link + "?pg=1#myTable"
            print(URL)
            while number <= pages:
                URL = URL[0:-9] + str(number) + "#myTable"
                pars = Parser(URL, "a", "chp-release")
                result = pars.parse()
                temp_dict = {i['title']: i['href'] for i in result}
                links.update(temp_dict)
                number += 1

        links.update({"url": self.__link})
        self.__full_library.update({self.__title: links})
        write("librarian", self.__full_library)

    def collect(self):
        links = self.full_library.get(self.__title)
        all_chapters = {}

        tag = input("tag: ")
        cl = input("cl: ")
        if tag == "":
            tag = 'div'
            cl = 'entry-content'
        else:
            link = input("link: ")
            write_txt('parser_links', f'{link}, {self.__title}, {tag}, {cl}\n')

        for k, v in links.items():
            if k != 'url':
                pars = Parser('https:' + v, tag, cl)
                result = pars.parse()
                temp_dict = {k: i.text for i in result}
                all_chapters.update(temp_dict)

        write(f'{self.__title}', all_chapters)

    def translate(self):
        chapter = input("Chapter: ")
        text = self.__chapters[chapter]
        write_txt(chapter, text)

        max_length = 10000
        substrings = []

        while len(text) > max_length:
            index = text.rfind(".", 0, max_length)
            if index == -1:
                index = max_length
            substrings.append(text[:index+1])
            text = text[index+1:]
            print(text)

        substrings.append(text)

        print(substrings)

        translator = Translator()

        for string in substrings:
            part = translator.translate(string)
            write_txt(chapter, part)
