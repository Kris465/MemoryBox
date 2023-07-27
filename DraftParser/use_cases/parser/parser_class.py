import re
from domain.project_class import Project
from presenter.database.session import get_session
from use_cases.parser.stepper_strategy import Stepper


class Parser:
    def __init__(self, project: Project) -> None:
        self.project = project

    def parse(self):
        temp_url = re.sub(r'^https?://(?:www\.)?(.*?)/.*$',
                          r'\1',
                          self.project.url)
        session = get_session()
        parser = session.query(Parser).filter_by(url=temp_url).first()
        if parser is not None:
            strategy_name = parser.strategy_name
            chapters = self.run_strategy(strategy_name, parser, self.project)
        else:
            params = {}
            cl = input("Введите класс: ")
            strategy = input("Введите название стратегии: ")
            if all(params.values()):
                chapters = self.run_custom_strategy(params)
                self.project.chapters = chapters
                new_parser = Parser(temp_url, cl, strategy)
                session.add(new_parser)
                session.close()
            else:
                raise ValueError("Не все параметры заполнены")

        return self.project

    def run_strategy(self, strategy_name, parser, project):
        if strategy_name == "stepper":
            sorted_chapters = sorted(project.chapters,
                                     key=lambda x: x.ordinal_number)
            strategy = Stepper(parser.cl, sorted_chapters)
        else:
            raise ValueError("Неизвестная стратегия")

        # Не передавать в метод агргументы!
        # Передавать все необходимые объекты в конструктор стратеги!
        chapters = strategy.collect_chapters()
        return chapters

    def run_custom_strategy(self, params):
        # Создание экземпляра пользовательской стратегии
        strategy = CustomStrategy(**params)
        # Запуск пользовательской стратегии с передачей нужных параметров
        chapters = strategy.get_chapters()
        return chapters
