import os
import re
from chapter import Chapter
from novel import Novel
from parser_class import Parser
from translator import Translator


class Controller:
    
    def __init__(self):
        self.__chapter = None
        self.__novel = None
        self.__parser_mod = None
        self.__translator_mod = None

    def new_novel(self):
        print("new_novel")

    def read_novel(self):
        print("read_novel")

    def update_novel(self):
        print("update_novel")
