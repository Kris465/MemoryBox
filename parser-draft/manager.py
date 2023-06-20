from typing import Optional
import re
from parser.chapter_class import Chapter
from db_session import get_session
from models import Chapters, Novel, Parser
from parser.collector_strategy import Collector
from drafts.stepper_strategy import Stepper


class Manager:
    def __init__(self, title: str) -> None:
        self.__title = title
        self.__chapter: Optional[Chapter] = None
        self.parser: Optional[Parser] = None

    def __str__(self) -> str:
        return f"Novel: {self.__title}, Chapter: {self.__chapter}"

    def __repr__(self) -> str:
        return f"Novel({self.__title})"

    def self_state(self):
        with get_session() as session:
            novel = session.query(Novel).filter_by(
                english_name=self.__title).first()
            if not novel:
                raise ValueError("Novel is not found")
            last_chapter = session.query(Chapters).filter_by(
                novel_id=novel.id).order_by(
                Chapters.ordinal_number.desc()).first()
            if not last_chapter:
                raise ValueError("Chapters is not found")
            self.__chapter = Chapter(
                ordinal_number=last_chapter.ordinal_number,
                link=last_chapter.link,
                language=last_chapter.language,
                original_text=last_chapter.original_text,
                russian_text=last_chapter.russian_text)
            temp_url = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1',
                              novel.webpage)
            self.parser = session.query(Parser).filter_by(url=temp_url).first()
            if self.parser is None:
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
            strategy_class = self.parser.strategy if self.parser else None
            if strategy_class == 'stepper':
                strategy = Stepper(self.__chapter, self.parser)
            elif strategy_class == 'collector':
                strategy = Collector(novel.webpage,
                                     self.__chapter,
                                     self.parser)
            else:
                strategy = None
            return strategy

    def collect_chapters(self) -> None:
        strategy = self.self_state()
        if strategy is None:
            raise ValueError("Strategy is not found")
        chapters = strategy.collect_chapters()
        with get_session() as session:
            novel = session.query(Novel).filter_by(
                english_name=self.__title).first()
            for chapter in chapters:
                new_chapter = Chapters(novel_id=novel.id,
                                       ordinal_number=chapter.ordinal_number,
                                       link=chapter.link,
                                       language=chapter.language,
                                       original_text=chapter.original_text,
                                       russian_text=chapter.russian_text)
                session.add(new_chapter)
            session.commit()
