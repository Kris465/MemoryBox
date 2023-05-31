

import time
from chapter_class import Chapter
from novel_class import Novel
from parser_class import Parser_
from project_class import Project
from repository_class import Repository


class Controller:

    def __init__(self, repository):
        self.__title = input("Title: ")
        self.repository = repository

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def repository(self):
        return self.__repository

    def info(self):
        language = self.repository.language()
        chapters_list = self.mod(language)

        if self.repository.find(self.__title):
            self.repository.show_table("....")
            # Соединение таблиц - Название, последняя глава, переведенная
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

    def mod(self, language):
        option = input("Collector mod? ")
        if option == "":
            self.collector_mod(language)
        else:
            self.stepper_mod(language)

    def collector_mod(self):
        pass

    def stepper_mod(self):
        chapters_list = []
        link = input("URL: ")
        pars = Parser_(link)
        pars.chapter = int(input("Chapter: "))

        while link is not None:
            time.sleep(5)
            if link[0] != 'h':
                pars.url = 'https:/' + link
            else:
                pars.url = link

            pars.check_tags()
            result = pars.parse()
            chapter = Chapter(pars.chapter,
                              pars.url,
                              str([i.text for i in result]))
            print(chapter.original_text)
            chapters_list.append(chapter)
            print(pars.chapter)
            link = pars.parse(return_url=True)
            pars.chapter += 1

        return chapters_list

    def delete(self):
        pass
