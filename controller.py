from database.db_session import get_session
from database.models import Chapters, Novel, Projects
from parser.manager import Manager
from translator.translator_class import Translator
from writer_to_txt import write_txt


class Controller:

    def __init__(self):
        self.__title = input("Title: ")

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    def parsing(self):
        pars = Manager(self.title)
        pars.collect_chapters()

    def create_project(self):
        session = get_session()
        status_num = input("Status: ")
        worker = input("Worker: ")
        rulate = input("Rulate: ")
        new_project = Projects(status_id=status_num,
                               worker_id=worker,
                               rulate=rulate)
        session.add(new_project)
        session.commit()
        session.close()

    def create_novel(self):
        rulate = input("Rulate: ")
        russian_name = input("Russian name: ")
        original_name = input("Original name: ")
        webpage = input("Webpage: ")
        session = get_session()
        result = session.query(Projects).filter(
            Projects.rulate == rulate).all()
        for project in result:
            novel = Novel(project_id=project.id,
                          russian_name=russian_name,
                          original_name=original_name,
                          english_name=self.title,
                          webpage=webpage)
        session.add(novel)
        session.commit()
        session.close()

    def delete(self):
        pass

    def translate(self):
        session = get_session()
        novel = session.query(Novel).filter(
            Novel.english_name == self.title).first()
        if not novel:
            print("Novel is not found")
            return

        # chapters = novel.chapters
        chapter_number = input("Chapter: ")
        chapter = session.query(Chapters).filter(
            Chapters.novel_id == novel.id,
            Chapters.ordinal_number == chapter_number).first()
        if not chapter:
            print("Chapter is not found")
            return

        text = chapter.original_text
        max_length = 10000
        substrings = []
        while len(text) > max_length:
            index = text.rfind(".", 0, max_length)
            # index = text.rfind("。", 0, max_length)
            if index == -1:
                index = max_length
            substrings.append(text[:index+1])
            text = text[index+1:]
            print(text)
        substrings.append(text)
        print(substrings)

        translator = Translator()
        translated_text = ""
        for string in substrings:
            part = translator.translate(string)
            translated_text += part

        write_txt(chapter_number, chapter.original_text)
        write_txt(chapter_number, translated_text)

        chapter.russian_text = translated_text
        session.commit()
        session.close()
