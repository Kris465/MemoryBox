from database.db_manager import DBManager
from parser.parser import Parser


class Controller:

    def logic(self):
        title = input("Title: ")

        db_manager = DBManager()
        project = db_manager.find(title)
        if project is None:
            url = input("url: ")
            # номер текущей главы
            # язык проекта, который собираемся парсить
            pars = Parser(title=title, project_webpage=url)
            pars.parse()
        else:
            project.update()
