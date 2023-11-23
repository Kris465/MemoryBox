import asyncio
from loguru import logger
from domain.file_tools import read, write, write_txt
from translator.translator_class import Translator


class TRManager:

    def __init__(self, language):
        self.language = language

    async def one_chapter(self, title, chapter=0):
        project = await asyncio.to_thread(read, f"{title}")
        text = project[str(chapter).strip()]
        await write_txt(chapter, text)
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
            part = await translator.translate(string, self.language)
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

    async def tr_from_to(self, title):
        start_chapter = int(input("From: "))
        last_chapter = int(input("To: "))
        full_chapters = {}
        while start_chapter <= last_chapter:
            one_chapter = await self.one_chapter(title, start_chapter)
            full_chapters.update(one_chapter)
            start_chapter += 1
        await write(title + "_translation", full_chapters, self.language)

    def get_sign(self, language):
        match language:
            case "zh":
                return "。"
            case "en":
                return "."
            case _:
                return "."
