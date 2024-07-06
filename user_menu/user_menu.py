import tkinter as tk
from tkinter import ttk


class Task:
    def __init__(self, task_type, title, link=None,
                 chapter=None, options=None, language=None):
        self.task_type = task_type
        self.title = title
        self.link = link
        self.chapter = chapter
        self.options = options
        self.language = language


class UserMenu:
    def __init__(self):
        self.tasks = []
        self.root = tk.Tk()
        self.root.title("Цербер")
        self.root.iconbitmap("user_menu/dog.ico")
        self.root.geometry("800x600+400+300")
        self.create_widgets()

    def create_widgets(self):
        self.left_frame = tk.Frame(self.root, bg='#FFCC99',
                                   width=600, height=800)
        self.left_frame.pack_propagate(False)
        self.left_frame.pack(side='left', fill='y')

        menu = tk.Menu(self.left_frame)
        menu.add_command(label="Собрать", command=self.collect)
        menu.add_command(label="Перевести", command=self.translate)
        self.left_frame.config(menu=menu)

        self.right_frame = tk.Frame(self.root, bg='#CC9966',
                                    width=200, height=400)
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side='right', fill='both', expand=True)

    def collect(self):
        # Действия при выборе "Собрать"
        pass

    def translate(self):
        # Действия при выборе "Перевести"
        pass

    # def submit_task(self):
    #     # Здесь можно добавить логику для обработки данных из полей ввода и выбранных опций
    #     pass

    def run(self):
        self.root.mainloop()
        return self.tasks
