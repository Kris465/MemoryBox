from reader_from_json import read
from writer_to_json import write
from parser_class import Parser

class Librarian():

    def __init__(self, title):
        self.__title = title
        self.__full_library = {}
        self.__link = None

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self):
        if self.__link is None:
            for key, value in self.__full_library.items():
                if key == self.__title:
                    self.__link = value[0]
        else:
            link = input("Link? \n")
            self.__link = link

    @property
    def full_library(self):
        return self.__full_library

    @full_library.setter
    def full_library(self):
        self.__full_library = read("library")

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

        self.__full_library.update({self.__title: [self.__link, links]})
        write("librarian", self.__full_library)
