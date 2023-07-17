from database.db_manager import DBManager
from parser.parser import Parser


class Controller:

    def logic(self):
        title = input("Title: ")

        db_manager = DBManager()
        project = db_manager.find(title)
        if project:
            project.update()
        else:
            url = input("url: ")
            number = int(input("chapter: "))
            pars = Parser(title, url, number)
            pars.parse()
