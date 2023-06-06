from db_session import get_session
from models import Chapters, Novel, Projects
from parser_class import Parser_
from translator_class import Translator
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

    def info(self):
        session = get_session()
        result = session.query(Novel).filter(
            Novel.english_name == self.title).first()
        if result:
            print("I found the novel. Update?")
            mod = input("stepper or collector?\n")
            language = input("eng or chi?\n")
            self.update(novel=result, mod=mod, language=language)
        else:
            option = int(input("I didn't find the novel. Create?\n"
                               "1. Project\n2. Novel\n"))
            if option == 1:
                self.create_project()
            elif option == 2:
                self.create_novel()
            else:
                return

    def update(self, novel=None, session=None, language=None, mod=None):
        if session is None:
            session = get_session()
        if novel is None:
            novel = session.query(Novel).filter(
                Novel.english_name == self.title).first()
        if mod is None:
            mod = input("stepper or collector?\n")
            language = input("eng or chi?\n")

        chapters = session.query(Chapters).filter(
                Chapters.novel_id == novel.id).all()
        if not chapters:
            last_ordinal_number = 0
        else:
            last_ordinal_number = chapters[-1].ordinal_number

        if mod == 'stepper':
            url = input("First link: ")
        else:
            url = novel.webpage

        pars = Parser_(url)
        pars.chapter = last_ordinal_number + 1

        parsed_chapters = pars.parse(mod, language)
        if not parsed_chapters:
            return

        new_chapters = []
        for chapter in parsed_chapters:
            # if chapter.link != chapters[-1].link:
            new_chapter = Chapters(novel_id=novel.id,
                                   ordinal_number=chapter.ordinal_number,
                                   language=language,
                                   link=chapter.link,
                                   original_text=chapter.original_text)
            new_chapters.append(new_chapter)
        session.add_all(new_chapters)
        session.commit()
        session.close()

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
