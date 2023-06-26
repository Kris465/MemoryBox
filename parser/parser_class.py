class Parser:
    def __init__(self, project):
        if project:
            self.project = project

    def parse(self):
        if isinstance(self.data, dict):
            # обработка словаря
            pass
        elif isinstance(self.data, Project):
            # обработка проекта
            pass
        else:
            # обработка других типов данных
            pass
