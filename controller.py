from db_session import get_session
from models import Chapters, Novel, Projects
from reader_from_json import read
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
            self.update(result)
        else:
            print("I didn't find the novel. Create?")
            option = input("I didn't find the novel. Create?\n"
                           "1. Project\n2. Novel")
            if option == 1:
                self.create_project()
            elif option == 2:
                self.create_novel()
            else:
                self.create_project()
                self.create_novel()

    def update(self, novel=None):
        if novel is None:
            session = get_session()
            novel = session.query(Novel).filter(
                Novel.english_name == self.title).first()
        
        chapters = session.query(Chapters).filter(
                Chapters.novel_id == novel.id).all()
        
        for

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
        chapter = input("Chapter: ")
        project = read(self.__title)
        text = project[chapter]
        write_txt(chapter, text)
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
        for string in substrings:
            part = translator.translate(string)
            write_txt(chapter, part)
