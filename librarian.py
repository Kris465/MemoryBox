import json
from reader_from_json import read
from writer_to_json import write
from parser_class import Parser

class Librarian():

    def __init__(self, title):
        self.__title = title
        self.__full_library = json.loads(open('librarian.json', encoding="UTF-8").read())
        self.__link = self.set_link(title)

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

    def add(self):
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
