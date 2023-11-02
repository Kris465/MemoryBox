import re

from loguru import logger
from parser.en_stepper import EnStepper
from parser.wx256_strategy import Wx256
from parser.wfxs_strategy import Wfxs
from parser.zh_shuka import ChiShuka
from parser.zh_82zg_strategy import Zg
from parser.zhuishukan_strategy import Zhuishukan


class Parser:
    def __init__(self, title: str, project_webpage: str):
        self.title = title
        self.project_webpage = project_webpage

    def parse(self):
        webpage_name = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1',
                              self.project_webpage)

        strategies = {
            EnStepper: ["wuxiap.com",
                        "vmnovels.com",
                        "mysticalmerries.com",
                        "sleepytranslations.com",
                        "salmonlatte.com",
                        "novelbin.org",
                        "akknovel.com",
                        "tnovelodyssey.blogspot.com",
                        "view.ridibooks.com",
                        "rainofsnow.com"],
            Wfxs: ["www.wfxs.com.tw"],
            Zhuishukan: ["m.zhuishukan.com"],
            ChiShuka: ["www.52shuku.vip"],
            Wx256: ["www.256wx.net"],
            Zg: ["www.82zg.com"]
        }
        for strategy, webpages in strategies.items():
            if webpage_name in webpages:
                strategy_instance = strategy(self.title, self.project_webpage)
                logger.info(f"Object of strategy {strategy} is created")
            else:
                strategy = input("Strategy?\n")
                try:
                    strategy_instance = strategy(self.title,
                                                 self.project_webpage)
                    strategies[strategy].append(webpage_name)
                    logger.info(f"Object of strategy {strategy} is created"
                                f"{webpage_name} added to webpages")
                except Exception:
                    logger.warning("We need a new strategy!")
                    return

            strategy_instance.logic()
