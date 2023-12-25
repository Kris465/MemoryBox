import asyncio
from typing import List

from loguru import logger
from domain.file_tools import read, write_txt
from domain.task import Task
from loader.for_rulate import ForRulate
from parser.parser import Parser
from translator.translator import TrManager


class Controller:
    def __init__(self, tasks: List[Task]) -> None:
        self.tasks = tasks

    async def parse(self, title, url, chapter) -> None:
        try:
            pars = Parser(title, url, chapter)
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

    async def save(self, title: str, url: str,
                   config_for_writing: int) -> None:
        text = ''
        try:
            project = await read(title + "_translation")
            flag = True
        except ValueError:
            project = await read(title)
            flag = False

        match config_for_writing:
            case 1:
                if flag:
                    for chapter, data in project.items():
                        text += chapter + '\n'.join(
                            str(value) for dictionary in data
                            for value in dictionary.values())
                else:
                    for k, v in project.items():
                        text += k + "\n" + v + "\n"

                await write_txt(title, text)
            case 2:
                for chapter, data in project.items():
                    if flag:
                        text = '\n'.join(str(value) for dictionary in data
                                         for value in dictionary.values())
                    else:
                        text += chapter + "\n" + data + "\n"

                    await write_txt(chapter + title, text)
            case 3:
                # database
                pass
            case 4:
                for_rulate = ForRulate(title, url, project)
                for_rulate.logic()

    async def execute_task(self, task: Task) -> None:
        if task.action == 1:
            await self.parse(task.title, url=task.extra, chapter=task.config)
        elif task.action == 2:
            await self.translate(task.title,
                                 language=task.extra,
                                 config=task.config)
        elif task.action == 3:
            await self.save(task.title, url=task.extra,
                            config_for_writing=task.config)

    async def run(self) -> None:
        tasks = [self.execute_task(task) for task in self.tasks]
        await asyncio.gather(*tasks)  # !!!
