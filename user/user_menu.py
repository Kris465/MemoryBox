from loguru import logger
from domain.task import Task


class UserMenu:
    def __init__(self) -> None:
        self.tasks = []

    def collect_user_input(self):
        print("What do you want to do, Master?\n")
        while True:
            title = input("Titlte: \n")
            option = int(input("1.Parse\n2.Translate\n3.Save\n4.Exit\n"))
            match option:
                case 1:
                    url = input("url: ")
                    task = Task(title, option, url)
                    self.tasks.append(task)
                    logger.info(f"task is created: {title} / parse / {url}")
                case 2:
                    language = input("language: ")
                    config = int(input("1.All\n2.From\n3.From-To\n"))
                    task = Task(title, option, language, config)
                    self.tasks.append(task)
                    logger.info(f"task is created: {title} / translate /"
                                f"{language} / {config}")
                case 3:
                    file_type = int(input("1.For chapters\n2.In one file\n"))
                    task = Task(title, option, file_type)
                    self.tasks.append(task)
                    logger.info(f"task is created: {title} / save /"
                                f"{file_type}")
                case _:
                    return self.tasks
