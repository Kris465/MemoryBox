from loguru import logger
from domain.file_tools import read, write
from translator.connector import Translator


class TrManager:
    '''
    option: list
    0 - function
    1 - start chapter
    2 - last chapter
    '''

    def __init__(self, title, language, option):
        self.title = title
        self.language = language
        self.option = option

    async def translate(self):
        func = self.option[0]
        if func == 1:
            logger.info(f"translate all / {self.title} / {self.language}")
            await self.translate_all()
        elif func == 2:
            logger.info(f"translate from / {self.title} / {self.language}")
            await self.translate_from()
        elif func == 3:
            logger.info(f"translate from-to / {self.title} / {self.language}")
            await self.translate_from_to()

    async def translate_all(self):
        full_chapters = {}
        project = await read(self.title)
        for chapter in project:
            text = project[chapter]
            tr_txt = await self.translate_text(text)
            full_chapters[chapter] = [{"origin": text},
                                      {"translation": tr_txt}]
            logger.info(f"{self.title} / {chapter} is translated")
        await write(self.title + "_translation", full_chapters, self.language)
        logger.info(f"json file with translation for {self.title} is written")

    async def translate_from(self):
        start_chapter = self.option[1]
        full_chapters = {}
        project = await read(self.title)
        for chapter in project:
            if int(chapter) >= start_chapter:
                text = project[chapter]
                tr_txt = await self.translate_text(text)
                full_chapters[chapter] = [{"origin": text},
                                          {"translation": tr_txt}]
                logger.info(f"{self.title} / {chapter} is translated")
        await write(self.title + "_translation", full_chapters, self.language)
        logger.info(f"json file with translation for {self.title} is written")

    async def translate_from_to(self):
        start_chapter = self.option[1]
        last_chapter = self.option[2]
        full_chapters = {}
        project = await read(self.title)
        for chapter, text in project.items():
            if start_chapter <= int(chapter) <= last_chapter:
                tr_txt = await self.translate_text(text)
                full_chapters[chapter] = [{"origin": text},
                                          {"translation": tr_txt}]
                logger.info(f"{self.title} / {chapter} is translated")
        await write(self.title + "_translation", full_chapters, self.language)
        logger.info(f"json file with translation for {self.title} is written")

    async def translate_text(self, text):
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
        tr_txt = ""
        for string in substrings:
            try:
                part = await translator.translate(string, self.language)
            except TypeError as e:
                logger.error(f"Error while translating {string}"
                             f"to {self.language}: {e}")
                part = " "
            tr_txt += part
        return tr_txt

    def get_sign(self, language):
        if language == "zh":
            return "。"
        else:
            return "."
