import random
import time

from loguru import logger
from reader import read
from translator.translator_class import Translator
from write_to_json import write
from writer_to_txt import write_txt


class TRManager():

    def __init__(self, language):
        self.language = language

    def one_chapter(self, title, chapter=0):
        project = read(title)
        text = project[str(chapter).strip()]
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
            tr_txt = ""
            part = translator.translate(string, self.language)
            if part is not None:
                write_txt(chapter, part)
                tr_txt += part
            else:
                break

        origin = text.translate(str.maketrans("", "", "\n\t"))
        trans = tr_txt.translate(str.maketrans("", "", "\n\t"))
        logger.info(f"{title} / {chapter} /"
                    "{}...{} / {}...{}".format(origin[:30], origin[-30:],
                                               trans[:30], trans[-30:]))
        return {chapter: [{"origin": text}, {"translation": tr_txt}]}

    def tr_from_to(self, title):
        start_chapter = int(input("From: "))
        last_chapter = int(input("To: "))
        full_chapters = {}
        while start_chapter <= last_chapter:
            one_chapter = self.one_chapter(title, start_chapter)
            full_chapters.update(one_chapter)
            time.sleep(random.randint(10, 30))
            start_chapter += 1
        write(title + "_translation", full_chapters, self.language)

    def get_sign(self, language):
        match language:
            case "zh":
                return "。"
            case "en":
                return "."
            case _:
                return "."
