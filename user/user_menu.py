from domain.task import Task

from loguru import logger


class UserMenu:
    def __init__(self):
        self.tasks = []

    def menu(self):
        print("What do you want to do, Master?\n")
        title = "something"
        kind = 0
        while title != "" or kind != 4:
            title = input("Title: \n")
            kind = int(input("1.Parse\n2.Translate\n3.Save\n4.Exit\n"))
            task = self.create_task(title, kind)
            self.tasks.append(task)
        return self.tasks

    def create_task(self, title, option):
        match option:
            case 1:
                url = input("url: ")
                chapter = int(input("chapter: \n"))
                task = Task(title, option, {"url": url, "chapter": chapter})
                logger.info(f"task is created: {title} / parse / {url}")
                return task
            case 2:
                language = input("language: ")
                temp = int(input("1.All\n2.From\n3.From-To"))
                if temp == 1:
                    task = Task(title, option, {"part": "all"})
                logger.info(f"task is created: {title} / translate /"
                            f"{language}")
                return task
            case 3:
                config_for_writing = int(input("1.in-one-file\n"
                                               "2.for-chapters\n"
                                               "3.database\n"
                                               "4.for-rulate\n"))
                task = Task(title, {"option": "save",
                                    "config_for_writing": config_for_writing})
                logger.info(f"task is created: {title} / save /"
                            f"{config_for_writing}")
                return task
            case 4:
                return
            case _:
                logger.error("User input invalid option")
                return self.create_task(
                    title, int(
                        input("1.Parse\n2.Translate\n3.Save\n4.Exit\n")))
