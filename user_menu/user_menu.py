import tkinter as tk


class CustomMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Цербер")
        self.root.geometry("600x500+400+200")
        self.root.iconbitmap("user_menu/dog.ico")

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        submenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Опции", menu=submenu)
        submenu.add_command(label="Опция 1", command=self.option1)
        submenu.add_command(label="Опция 2", command=self.option2)
        submenu.add_separator()
        submenu.add_command(label="Выход", command=self.root.quit)

    def option1(self):
        print("Вы выбрали опцию 1")
        # Здесь можно добавить код для обработки опции 1

    def option2(self):
        print("Вы выбрали опцию 2")
        # Здесь можно добавить код для обработки опции 2

    def run(self):
        self.root.mainloop()
