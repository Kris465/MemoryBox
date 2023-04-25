import os
import re
from chapter import Chapter
from novel import Novel
from parser_class import Parser
from translator import Translator
from librarian import Librarian


class Controller:

    def librarian(self, title):
        title = input("Title: \n")
        librarian = Librarian(title)
        librarian.add()
