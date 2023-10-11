# from database.db_manager import DBManager
from parser.parser import Parser
from reader_from_json import read
from translator.tr_manager import TRManager
from writer_to_txt import write_txt


class Controller:

    def logic(self):
        title = input("Title: ")

        option = int(input("1. Parse\n2. Translate\n3. Write.\n"))
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
            case 3:
                project = read(title + "_translation")
                translated_text = ''
                for chapter in project.values():
                    for text in chapter:
                        translated_text += text.get("translation", '')
                write_txt(title, translated_text)
