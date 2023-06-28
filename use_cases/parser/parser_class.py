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
            chapters = self.run_strategy(strategy_name, parser)
        else:
            tag = input("Введите тег: ")
            cl = input("Введите класс: ")
            word = input("Введите слово: ")
            strategy_name = input("Введите название стратегии: ")
            chapters = self.run_custom_strategy(tag,
                                                cl,
                                                word,
                                                strategy_name)
        self.project.chapters = chapters
        return self.project

    def run_strategy(self, strategy_name, parser):
        if strategy_name == "stepper":
            strategy = Stepper(parser, self.project.chapters)
        else:
            raise ValueError("Неизвестная стратегия")

        # Запуск стратегии с передачей нужных параметров
        chapters = strategy.collect_chapters()
        return chapters

    def run_custom_strategy(self, tag, class_name, word, strategy_name):
        # Создание экземпляра пользовательской стратегии
        strategy = CustomStrategy(tag, class_name, word)

        # Запуск пользовательской стратегии с передачей нужных параметров
        chapters = strategy.get_chapters(self.project.webpage)
        return chapters
