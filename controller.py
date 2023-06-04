from sqlalchemy import inspect
from db_session import get_session
from models import Novel, Projects
from parser_class import Parser_
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
            self.update()
        else:
            print("I didn't find the novel. Create?")
            self.create()

    def update(self):
        pass

    def create(self):
        session = get_session()
        status_num = input("Status: ")
        worker = input("Worker: ")
        rulate = input("Rulate: ")
        new_project = Projects(status_id=status_num,
                               worker_id=worker,
                               rulate=rulate)
        session.add(new_project)
        russian_name = input("Russian name: ")
        original_name = input("Original name: ")
        english_name = self.title
        webpage = input("Webpage: ")
        novel = Novel(project_id=new_project,
                      russian_name=russian_name,
                      original_name=original_name,
                      english_name=english_name,
                      webpage=webpage)
        
        session.add(novel)
        session.commit()
        session.close()

    # def create(self, chapters_list=None):
    #     self.repository.show_table("status")
    #     status_num = input("Status: ")
    #     self.repository.show_table("workers")
    #     worker = input("Worker: ")
    #     rulate = input("Rulate: ")
    #     project = Project(status_num, worker, rulate)

    #     russian_name = input("Russian name: ")
    #     original_name = input("Original name: ")
    #     english_name = self.title
    #     webpage = input("Webpage: ")
    #     novel = Novel(russian_name, original_name, english_name, webpage)

    #     decision = input("Save to db? ")
    #     if decision == "":
    #         self.repository.save_objects(project, novel, chapters_list)

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
