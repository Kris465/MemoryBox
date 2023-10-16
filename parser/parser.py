from parser.en_stepper import EnStepper
from parser.wx256_strategy import Wx256
from parser.wfxs_strategy import Wfxs
from parser.zh_shuka import ChiShuka
from parser.novelupdates_strategy import NovelUpdates
from parser.zh_82zg_strategy import Zg
from parser.zhuishukan_strategy import Zhuishukan


class Parser:
    def __init__(self,
                 title,
                 chapter=None,
                 url="",
                 project_webpage="",
                 number=1):
        self.title = title
        self.url = url
        self.chapter = chapter
        self.project_webpage = project_webpage
        self.number = number

    def parse(self):
        if "www.novelupdates.com" in self.project_webpage:
            strategy = NovelUpdates(self.title,
                                    self.project_webpage,
                                    self.number)
        elif "www.wfxs.com.tw" in self.project_webpage:
            strategy = Wfxs(self.title,
                            self.project_webpage,
                            self.number)
        elif "m.zhuishukan.com" in self.project_webpage:
            strategy = Zhuishukan(self.title,
                                  self.project_webpage,
                                  self.number)
        elif "www.52shuku.vip" in self.project_webpage:
            strategy = ChiShuka(self.title,
                                self.project_webpage,
                                self.number)
        elif "www.256wx.net" in self.project_webpage:
            strategy = Wx256(self.title,
                             self.project_webpage,
                             self.number)
        elif "www.82zg.com" in self.project_webpage:
            strategy = Zg(self.title,
                          self.project_webpage)
        elif self.project_webpage in []:
            strategy = EnStepper(self.title,
                                 self.project_webpage)
        else:
            return

        strategy.logic()
