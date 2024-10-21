import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox


class UserMenu:
    def __init__(self) -> None:
        self.tasks = []
        self.root = tk.Tk()
        self.root.title("Цербер")
        self.root.geometry("800x600+400+300")
        self.main_menu = Menu(self.root)


    def run(self):
        self.root.mainloop()
        return self.tasks
