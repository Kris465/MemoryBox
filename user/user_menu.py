from loguru import logger
from domain.task import Task


class UserMenu:
    def __init__(self):
        self.tasks = []

    def menu(self):
        print("What do you want to do, Master?\n")
        task = ""
        option = ""
        while task is not None and option != 4:
            title = input("Title: \n")
            option = int(input("1.Parse\n2.Translate\n3.Save\n4.Exit\n"))
            task = self.create_task(title, option)
            if task is not None:
                self.tasks.append(task)
        return self.tasks

    def create_task(self, title, option):
        match option:
            case 1:
                url = input("url: ")
                try:
                    chapter = int(input("chapter: "))
                    task = Task(title, option, url, chapter)
                except ValueError:
                    task = Task(title, option, url)
                logger.info(f"task is created: {title} / parse / {url}")
                return task
            case 2:
                language = input("language: ")
                config = int(input("1.All\n2.From\n3.From-To\n"))
                task = Task(title, option, language, config)
                logger.info(f"task is created: {title} / translate /"
                            f"{language} / {config}")
                return task
            case 3:
                file_type = int(input("1.For chapters\n2.In one file\n"))
                task = Task(title, option, file_type)
                self.tasks.append(task)
                logger.info(f"task is created: {title} / save /"
                            f"{file_type}")
                return task
            case 4:
                return
            case _:
                logger.error("User input invalid option")
                return self.create_task(
                    title, int(
                        input("1.Parse\n2.Translate\n3.Save\n4.Exit\n")))
