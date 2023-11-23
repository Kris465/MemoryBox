import re

from loguru import logger

from domain.file_tools import read
from .strategies import strategy_class


class Parser:
    def __init__(self, title: str, project_webpage: str):
        self.title = title
        self.project_webpage = project_webpage

    async def parse(self):
        webpage_name = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1',
                              self.project_webpage)
        logger.info(f"Webpage name is {webpage_name}")
        library = await read("library")

        if webpage_name in library:
            strategy_name = library[webpage_name][1]["strategy"]
            logger.info(f"{self.project_webpage} / {strategy_name}")
            strategy = strategy_class(strategy_name,
                                      self.title,
                                      self.project_webpage)
            logger.info(f"Object {strategy.__class__.__name__} is created")
        else:
            strategy_name = input("Strategy?\n")
            try:
                strategy = strategy_class(strategy_name,
                                          self.title,
                                          self.project_webpage)
            except KeyError:
                logger.debug(f"Create strategy for {self.project_webpage}")
                return

        await strategy.logic()
