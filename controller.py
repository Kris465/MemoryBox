# import time
from parser_class import Parser_
from reader_from_json import read
from translator import Translator
from writer_to_json import write
from writer_to_txt import write_txt


class Controller:

    def __init__(self):
        self.__title = input("Title: ")

    def find(self):
        # Если есть новела в бд, предлагаем обновить (задать настройки:
        # ссылка на сайт, порядковый номер главы)
        # Иначе - предлагаем создать проект, получаем все вводные данные.
        pass

    def create(self):
        all_chapters = {}
        number = 1
        URL = input("URL: ")
        pars = Parser_(URL)
        stepper = Parser_(URL)
        temp_url = stepper.find_button()
        result = pars.parse()
        if len(result) < 500:
            pars.check_tags()

        temp_dict = {number: i.text for i in result}
        all_chapters.update(temp_dict)

        while temp_url is not None:
            pars.url = temp_url
            result = pars.parse()
            stepper.url = temp_url
            temp_url = stepper.find_button()
            temp_dict = {number: i.text for i in result}
            all_chapters.update(temp_dict)
            number += 1

        write(self.__title, all_chapters)

    def update(self):
        pass

    def translate(self):
        chapter = input("Chapter: ")
        project = read(self.__title)
        text = project[chapter]
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
