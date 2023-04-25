import os
import re
from chapter import Chapter
from novel import Novel
from parser_class import Parser
from translator import Translator
from librarian import Librarian


class Controller:

    def __init__(self):
        self.__chapter = None
        self.__novel = None
        self.__parser_mod = None
        self.__translator_mod = None

    def new_novel(self):
        title = input("Title: \n")
        librarian = Librarian(title)
        librarian.add()

    def read_novel(self):
        print("read_novel")

    def update_novel(self):
        print("update_novel")
