from parser.Wx256 import Wx256
from parser.wfxs_strategy import Wfxs
from parser.chi_shuka import ChiShuka
from parser.novelupdates_strategy import NovelUpdates
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

    def parse(self):  # Надо доделать класс
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
        else:
            return

        strategy.logic()
