import re
from loguru import logger
from domain.file_tools import read, write
from domain.task import Task


class UserMenu:
    def __init__(self):
        self.tasks = []
        self.library = self.librarian

    def menu(self):
        print("What do you want to do, Master?\n")
        task = ""
        option = ""
        while task is not None and option != 4:
            title = input("Title: \n")
            option = int(input("1.Parse\n2.Translate\n3.Save\n4.Exit\n"))
            if option == 4 or title == "":
                break
            else:
                task = self.create_task(title, option)
                self.tasks.append(task)
        return self.tasks

    def create_task(self, title, option):
        match option:
            case 1:
                url = input("url: ")
                chapter = int(input("chapter: "))
                webpage_name = re.sub(r'^https?://(?:www\.)?(.*?)/.*$', r'\1',
                                      url)
                tag_sets = self.check(webpage_name)
                if tag_sets[1]["strategy"] == 'DIY':
                    links = [input("url: ") for _ in iter(int, 1)]
                    task = Task(title, option, chapter, links)

                try:
                    task = Task(title, option, url, chapter)
                except ValueError:
                    task = Task(title, option, url)
                logger.info(f"task is created: {title} / parse / {url}")
                return task
            case 2:
                language = input("language: ")
                print("Input config data in spaces\n"
                      "1.All\n2.From\n3.From-To")
                config = [int(num) for num in input().split()]
                task = Task(title, option, language, config)
                logger.info(f"task is created: {title} / translate /"
                            f"{language} / {config}")
                return task
            case 3:
                language = input("Language: \n")
                config_for_writing = int(input("1.in-one-file\n"
                                               "2.for-chapters\n"
                                               "3.database\n"))
                task = Task(title, option, language, config_for_writing)
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

    async def check(self, webpage_name):
        try:
            tag_sets = self.library[webpage_name]
        except KeyError:
            temp_dict = {webpage_name: [{"tag": input("tag: "),
                                         "extra_tag": input("extra_tag: "),
                                         "word": input("word: ")},
                                        {"strategy": "EnStepper"}]}
            dictionary = self.library
            dictionary.update(temp_dict)
            await write("library", dictionary)
            tag_sets = temp_dict[webpage_name]
        return tag_sets

    async def librarian(self):
        return await read("library")
