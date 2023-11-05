# from database.db_manager import DBManager
from loguru import logger
from parser.parser import Parser
from reader import read
from translator.tr_manager import TRManager
from writer_to_txt import write_txt


class Controller:
    def __init__(self, title):
        self.title = title

    async def logic(self):
        print(self.title)
        option = int(input("1. Parse\n2. Translate\n3. Write\n4. Exit\n"))
        match option:
            case 1:
                await self.parse()
            case 2:
                await self.translate()
            case 3:
                await self.write()
            case _:
                return

    async def parse(self):
        print(self.title)
        url = input("url: ")
        pars = Parser(title=self.title, project_webpage=url)
        logger.info(f"Parsing / {self.title} / {url}")
        await pars.parse()

    async def translate(self):
        print(self.title)
        language = input("language: ")
        trans = TRManager(language)
        trans.tr_from_to(self.title)
        logger.info(f"translating / {self.title} / {language}")

    async def write(self):
        project = read(self.title + "_translation")
        translated_text = ''
        for chapter in project.values():
            for text in chapter:
                translated_text += text.get("translation", '')
        write_txt(self.title, translated_text)
        logger.info(f"{self.title} has written to file")
