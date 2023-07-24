# import re
# from database.db_session import get_session
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
        else:
            strategy = ChiShuka(self.title,
                                self.project_webpage,
                                self.number)

        strategy.logic()

    # def choose_strategy(self):
    #     return strategy

    # def check(self, url):
    #     print("Checking tags...")
    #     temp_url = re.sub(r'^https?://(?:www\.)?(.*?)/.*$',
    #                       r'\1',
    #                       url)
    #     print(temp_url)
    #     session = get_session()
    #     result = session.query(Parser).filter(Parser.url == temp_url).all()
    #     if result:
    #         for webpage in result:
    #             cl = webpage.cl
    #             other = webpage.other
    #             word = webpage.word
    #             best_strategy = webpage.strategy
    #             print(cl, other, word, best_strategy)
    #     else:
    #         cl = input("class: ")
    #         other = input("other sings: ")
    #         word = input("word: ")
    #         strategy = input("best strategy: ")
    #         new_webpage = Parser(url=temp_url,
    #                              cl=cl,
    #                              other=other,
    #                              word=word,
    #                              strategy=strategy)
    #         session.add(new_webpage)
    #         session.commit()
