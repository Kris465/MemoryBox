from domain.db_manager import DBManager
from presenter.user_menu.view import View
from presenter.write_read_files.writer_to_json import write
from use_cases.parser.parser_class import Parser


class Controller:

    def __init__(self, view: View):
        self.view = view

    def logic(self):
        title = self.view.get_info("Title: ")
        try:
            db_manager = DBManager()
            project = db_manager.find(title)
        except Exception:
            project = self.view.ask_user(title)

        pars = Parser(project)
        project = pars.parse()
        # trans = Translator(project)
        # project = trans.translate()

        write(project.english_name, str(project.__dict__))
        # db_manager = DBManager()
        # db_manager.save(project)
