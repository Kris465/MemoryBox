# from database.db_manager import DBManager
from parser.parser import Parser
from translator.tr_manager import TRManager


class Controller:

    def logic(self):
        title = input("Title: ")

        option = int(input("1. Parse\n2. Translate\n"))
        match option:
            case 1:
                url = input("url: ")
                # number = int(input("Chapter: "))
                pars = Parser(title=title, project_webpage=url)
                # pars = Parser(title=title, number=number, url=url)
                pars.parse()
            case 2:
                language = input("language: ")
                trans = TRManager(language)
                trans.tr_from_to(title)

        # db_manager = DBManager()
        # project = db_manager.find(title)
        # if project is None:
        #     url = input("url: ")
        #     # номер текущей главы
        #     # язык проекта, который собираемся парсить
        #     pars = Parser(title=title, project_webpage=url)
        #     pars.parse()
        #     trans = TRManager(title)
        #     option = int(input(
        #         "1. Translate one chapter.\n2. Translate from-to.\n"))
        #     match option:
        #         case 1:
        #             trans.one_chapter(title)
        #         case 2:
        #             trans.tr_from_to(title)
        # else:
        #     project.update()
