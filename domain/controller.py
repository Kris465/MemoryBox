import asyncio
from typing import List

from loguru import logger
from domain.file_tools import read, write_txt
from domain.task import Task
from parser.parser import Parser
from translator.translator import TrManager


class Controller:
    def __init__(self, tasks: List[Task]) -> None:
        self.tasks = tasks

    async def parse(self, title: str, url: str) -> None:
        try:
            pars = Parser(title, url)
            await pars.parse()
            await asyncio.sleep(5)
            logger.info(f"Parsing {title} / {url} completed")
        except Exception as e:
            logger.error(f"Error while parsing {title} / {url}: {e}")

    async def translate(self, title: str, language: str, config: list) -> None:
        try:
            trans = TrManager(title, language, config)
            await trans.translate()
            await asyncio.sleep(3)
            logger.info(f"Translation to {language} / {title} completed")
        except Exception as e:
            logger.error(f"Error while translating {title} to {language}: {e}")

    async def save(self, title: str, file_type: str) -> None:
        # обратить внимание на запись в файл в классе переводчика
        project = await read(title + "_translation")
        translated_text = ''
        for chapter in project.values():
            for text in chapter:
                translated_text += text.get("translation", '')
        await write_txt(title, translated_text)
        logger.info(f"{title} has written to file")
        await asyncio.sleep(2)
        logger.info(f"Text saved as {file_type}")

    async def execute_task(self, task: Task) -> None:
        if task.action == 1:
            await self.parse(task.title, url=task.extra)
        elif task.action == 2:
            await self.translate(task.title,
                                 language=task.extra,
                                 config=task.config)
        elif task.action == 3:
            await self.save(task.title, file_type=task.extra)

    async def run(self) -> None:
        tasks = [self.execute_task(task) for task in self.tasks]
        await asyncio.gather(*tasks)
