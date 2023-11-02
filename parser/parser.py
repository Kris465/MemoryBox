import re

from loguru import logger
from parser.en_stepper import EnStepper
from parser.wx256_strategy import Wx256
from parser.wfxs_strategy import Wfxs
from parser.zh_shuka import ChiShuka
from parser.zh_82zg_strategy import Zg
from parser.zhuishukan_strategy import Zhuishukan
from reader import read


class Parser:
    def __init__(self, title: str, project_webpage: str):
        self.title = title
        self.project_webpage = project_webpage

    def parse(self):
        webpage_name = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1',
                              self.project_webpage)
        logger.info(f"Webpage name is {webpage_name}")
        library = read("library")

        if webpage_name in library:
            val = library[webpage_name]
            strategy_class = val[1].get("strategy")
            logger.info(f"{self.project_webpage} / {val} / {strategy_class}")
            strategy = strategy_class(self.title, self.project_webpage)
            logger.info(f"Object {strategy.__class__.__name__} is created")
        else:
            strategy_name = {"strategy": input("Strategy?\n")}
            try:
                strategy_class = strategy_name.get("strategy")
                strategy = strategy_class(self.title, self.project_webpage)
            except Exception:
                logger.debug(f"Create strategy for {self.project_webpage}")
                return

        strategy.logic()
