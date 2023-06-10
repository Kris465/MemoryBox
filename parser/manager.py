import re
from chapter_class import Chapter
from db_session import get_session
from models import Chapters, Novel, Parser
from modules.writer_to_json import write
from parser.collector_strategy import Collector
from parser.stepper_strategy import Stepper


class Manager():
    def __init__(self, title):
        self.__title = title
        self.__chapter = None

    @property
    def title(self):
        return self.__title

    @property
    def chapter(self):
        return self.__chapter

    def self_state(self):
        session = get_session()
        novel = session.query(Novel).filter_by(english_name=self.title).first()
        if not novel:
            print("Novel is not found")
            return None
        last_chapter = session.query(
            Chapters).filter_by(
            novel_id=novel.id).order_by(
            Chapters.ordinal_number.desc()).first()
        self.__chapter = Chapter(ordinal_number=last_chapter.ordinal_number,
                                 link=last_chapter.link,
                                 language=last_chapter.language,
                                 original_text=last_chapter.original_text,
                                 russian_text=last_chapter.russian_text)
        temp_url = re.sub(r'^https?://(?:www\.)?(.*?)/.*$',
                          r'\1',
                          novel.webpage)
        parser_data = session.query(Parser).filter_by(url=temp_url).first()
        if not parser_data:
            tag = input("tag: ")
            cl = input("class: ")
            word = input("word: ")
            strategy = input("strategy: ")
            new_webpage = Parser(url=temp_url,
                                 tag=tag,
                                 cl=cl,
                                 word=word,
                                 strategy=strategy)
            session.add(new_webpage)
            session.commit()
            session.close()
        strategy_class = parser_data.strategy
        match strategy_class:
            case None:
                strategy = input("Strategy: ")
            case 'stepper':
                strategy = Stepper(self.chapter)
            case 'collector':
                strategy = Collector(novel.webpage, self.chapter)
        return strategy

    def collect_chapters(self):
        strategy_obj = self.self_state()
        chapters1 = strategy_obj.collect_chapters()
        write(self.title + "st", chapters1)

    # def check_tags(self):
    #     print("Checking tags...")
    #     temp_url = re.sub(r'^https?://(?:www\.)?(.*?)/.*$',
    #                       r'\1',
    #                       self.__url)
    #     print(temp_url)
    #     session = get_session()
    #     result = session.query(Parser).filter(Parser.url == temp_url).all()
    #     if len(result) == 1:
    #         for webpage in result:
    #             self.__tag = webpage.tag
    #             self.__cl = webpage.cl
    #             self.__word = webpage.word
    #             print(self.tag, self.cl, self.word)
    #     elif len(result) == 0:
    #         self.__tag = input("tag: ")
    #         self.__cl = input("class: ")
    #         self.__word = input("word: ")
    #         new_webpage = Parser(url=temp_url,
    #                              tag=self.__tag,
    #                              cl=self.__cl,
    #                              word=self.__word)
    #         session.add(new_webpage)
    #         session.commit()
    #     else:
    #         print("Check datebase!!!")
