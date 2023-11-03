# from database.db_manager import DBManager
import asyncio
from loguru import logger
from parser.parser import Parser
from reader import read
from translator.tr_manager import TRManager
from writer_to_txt import write_txt


class Controller:
    def __init__(self, title):
        self.title = title

    async def logic(self):
        while True:
            option = int(input("1. Parse\n2. Translate\n3. Write\n4. Exit\n"))
            if option == 1:
                await self.parse()
            elif option == 2:
                await self.translate()
            elif option == 3:
                await self.write()
            elif option == 4:
                break

    async def parse(self):
        print(self.title)
        url = input("url: ")
        pars = Parser(title=self.title, project_webpage=url)
        logger.info(f"Parsing / {self.title} / {url}")
        await asyncio.sleep(20)
        pars.parse()

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
