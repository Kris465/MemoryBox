from novel_class import Novel
from parser_class import Parser_
from project_class import Project
from reader_from_json import read
from translator_class import Translator
from writer_to_txt import write_txt


class Controller:

    def __init__(self, repository):
        self.__title = input("Title: ")
        self.__repository = repository

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def repository(self):
        return self.__repository

    @repository.setter
    def repository(self, repository):
        self.__repository = repository

    def info(self):
        url = input("url: ")
        pars = Parser_(url)
        chapters_list = pars.parse("collector", "chi")
        if self.repository.find(self.__title):
            self.update(chapters_list)
        else:
            self.create(chapters_list)

    def update(self, chaptes_list):
        pass

    def create(self, chapters_list):
        self.repository.show_table("status")
        status_num = input("Status: ")
        self.repository.show_table("workers")
        worker = input("Worker: ")
        rulate = input("Rulate: ")
        project = Project(status_num, worker, rulate)

        russian_name = input("Russian name: ")
        original_name = input("Original name: ")
        english_name = input("English name: ")
        webpage = input("Start page: ")
        novel = Novel(russian_name, original_name, english_name, webpage)

        self.repository.write(project, novel, chapters_list)
        decision = input("Save to db? ")
        if decision == "":
            self.repository.save(project, novel, chapters_list)

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
