import random
import time
from reader_from_json import read
from translator.translator_class import Translator
from writer_to_txt import write_txt


class TRManager():

    def __init__(self, language):
        self.language = language

    def one_chapter(self, title, chapter=0):
        project = read(title)
        text = project[str(chapter)]
        write_txt(chapter, text)
        max_length = 10000
        substrings = []
        sign = self.get_sign(self.language)

        while len(text) > max_length:
            index = text.rfind(sign, 0, max_length)
            if index == -1:
                index = max_length
            substrings.append(text[:index+1])
            text = text[index+1:]

        if len(text) > 0:
            substrings.append(text)

        translator = Translator()
        for string in substrings:
            part = translator.translate(string, self.language)
            if part is not None:
                write_txt(chapter, part)
            else:
                part = translator.translate(string, self.language)

    def tr_from_to(self, title):
        start_chapter = int(input("From: "))
        last_chapter = int(input("To: "))
        while start_chapter <= last_chapter:
            self.one_chapter(title, start_chapter)
            time.sleep(random.randint(10, 360))
            start_chapter += 1

    def get_sign(self, language):
        match language:
            case "zh":
                return "。"
            case "en":
                return "."
            case _:
                return "."
