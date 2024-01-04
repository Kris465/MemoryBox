import tkinter as tk

from domain.task import Task


class UserMenu:
    def __init__(self, storage):
        self.tasks = []
        self.storage = storage
        self.window = tk.Tk()
        self.window.title("Task Manager")

        self.title_label = tk.Label(self.window, text="Title:")
        self.title_label.pack()

        self.title_entry = tk.Entry(self.window)
        self.title_entry.pack()

        self.option_label = tk.Label(self.window, text="Description:")
        self.option_label.pack()

        self.option_entry = tk.Entry(self.window)
        self.option_entry.pack()

        self.url_label = tk.Label(self.window, text="Priority:")
        self.url_label.pack()

        self.create_button = tk.Button(self.window, text="Create Task",
                                       command=self.create_task)
        self.create_button.pack()

    def create_task(self):
        title = self.title_entry.get()
        description = self.url_entry.get()
        priority = int(self.chapter_entry.get())
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.storage.add_task(task)

    def run(self):
        self.window.mainloop()

# from loguru import logger
# from domain.task import Task


# class UserMenu:
#     def __init__(self):
#         self.tasks = []

#     def menu(self):
#         print("What do you want to do, Master?\n")
#         task = ""
#         option = ""
#         while task is not None and option != 4:
#             title = input("Title: \n")
#             option = int(input("1.Parse\n2.Translate\n3.Save\n4.Exit\n"))
#             if option == 4 or title == "":
#                 break
#             else:
#                 task = self.create_task(title, option)
#                 self.tasks.append(task)
#         return self.tasks

#     def create_task(self, title, option):
#         match option:
#             case 1:
#                 url = input("url: ")
#                 chapter = int(input("chapter: \n"))
#                 try:
#                     task = Task(title, option, url, chapter)
#                 except ValueError:
#                     task = Task(title, option, url)
#                 logger.info(f"task is created: {title} / parse / {url}")
#                 return task
#             case 2:
#                 language = input("language: ")
#                 print("Input config data in spaces\n"
#                       "1.All\n2.From\n3.From-To")
#                 config = [int(num) for num in input().split()]
#                 task = Task(title, option, language, config)
#                 logger.info(f"task is created: {title} / translate /"
#                             f"{language} / {config}")
#                 return task
#             case 3:
#                 language = input("option: \n")
#                 config_for_writing = int(input("1.in-one-file\n"
#                                                "2.for-chapters\n"
#                                                "3.database\n"
#                                                "4.for-rulate\n"))
#                 task = Task(title, option, language, config_for_writing)
#                 logger.info(f"task is created: {title} / save /"
#                             f"{config_for_writing}")
#                 return task
#             case 4:
#                 return
#             case _:
#                 logger.error("User input invalid option")
#                 return self.create_task(
#                     title, int(
#                         input("1.Parse\n2.Translate\n3.Save\n4.Exit\n")))
