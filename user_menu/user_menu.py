import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


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
        self.root.geometry("800x600+400+300")
        self.create_widgets()

    def create_widgets(self):
        self.left_frame = tk.Frame(self.root, bg='#FFCC99', width=600, height=800)
        self.left_frame.pack_propagate(False)
        self.left_frame.pack(side='left', fill='y')

        # Добавляем внутренний фрейм для разделения по горизонтали
        inner_frame_top = tk.Frame(self.left_frame, bg='#FFCC99', width=600, height=400)
        inner_frame_top.pack_propagate(False)
        inner_frame_top.pack(side='top', fill='both', expand=True)

        inner_frame_bottom = tk.Frame(self.left_frame, bg='#FFCC99', width=600, height=400)
        inner_frame_bottom.pack_propagate(False)
        inner_frame_bottom.pack(side='top', fill='both', expand=True)

        # Ваши существующие виджеты могут быть добавлены в один из внутренних фреймов

    def toggle_blocks(self):
        pass

    def collect(self):
        messagebox.showinfo("Действие", "Функция 'Собрать' вызвана")

    def translate(self):
        messagebox.showinfo("Действие", "Функция 'Перевести' вызвана")


    def run(self):
        self.root.mainloop()
        return self.tasks
