import time
from parser_class import Parser_
from reader_from_json import read
from translator_class import Translator
from writer_to_json import write
from writer_to_txt import write_txt


class Controller:

    def __init__(self):
        self.__title = input("Title: ")

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

    def collect_chapters(self):
        all_chapters = {}
        temp_url = input("URL: ")
        pars = Parser_(temp_url)

        while temp_url is not None:
            time.sleep(5)
            print(pars.chapter)
            if temp_url[0] != 'h':
                pars.url = 'https:/' + temp_url
            else:
                pars.url = temp_url

            pars.check_tags()
            result = pars.parse()
            temp_dict = {pars.chapter: pars.url + i.text for i in result}
            print(temp_dict)
            all_chapters.update(temp_dict)
            write(self.__title, all_chapters)
            temp_url = pars.parse(return_url=True)
            pars.chapter += 1
