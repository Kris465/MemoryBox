import asyncio
from typing import List

from loguru import logger
from domain.task import Task
from parser.parser import Parser
from reader import read
from translator.tr_manager import TRManager
from writer_to_txt import write_txt


class Controller:
    def __init__(self, tasks: List[Task]) -> None:
        self.tasks = tasks

    async def parse(self, title: str, url: str) -> None:
        pars = Parser(title, url)
        await pars.parse()
        await asyncio.sleep(5)
        logger.info(f"Parsing {title} / {url} completed")

    async def translate(self, title: str, language: str, config: int) -> None:
        # видоизменить классы переводчика и переписать метод translate()
        trans = TRManager(language, config)
        await trans.translate(title)
        await asyncio.sleep(3)
        logger.info(f"Translation to {language} / {title} completed")

    async def save(self, title: str, file_type: int) -> None:
        # обратить внимание на запись в файл в классе переводчика
        project = read(title + "_translation")
        translated_text = ''
        for chapter in project.values():
            for text in chapter:
                translated_text += text.get("translation", '')
        write_txt(title, translated_text)
        logger.info(f"{title} has written to file")
        await asyncio.sleep(2)
        logger.info(f"Text saved as {file_type}")

    async def execute_task(self, task: Task) -> None:
        if task.option == 1:
            await self.parse(task.title, task.url)
        elif task.option == 2:
            await self.translate(task.title, task.language, task.config)
        elif task.option == 3:
            await self.save(task.title, task.file_type)

    async def run(self) -> None:
        tasks = [self.execute_task(task) for task in self.tasks]
        await asyncio.gather(*tasks)
