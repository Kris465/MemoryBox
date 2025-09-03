import tkinter as tk


class UserMenu:
    def __init__(self, tasks_collection) -> None:
        self.tasks_collection = tasks_collection

        self.root = tk.Tk()
        self.root.title("Генератор заданий")
        self.root.geometry("600x500+500+400")
        self.root.configure(bg='#FF00FF')

        self.task_label = tk.Label(self.root, text="Программа, задание",
                                   font=("Comic Sans MS", 24),
                                   bg='#9932CC',
                                   wraplength=500)
        self.task_label.pack(expand=True, fill='both', padx=20, pady=(50, 0))

        self.next_button = tk.Button(self.root, text="Следующее задание",
                                     command=self.show_next_task)
        self.next_button.pack(side='bottom', fill='x', padx=20, pady=10)

        self.show_next_task()

    def show_next_task(self):
        if self.tasks_collection:
            next_task_key = next(iter(self.tasks_collection))
            task_text = self.tasks_collection.pop(next_task_key)
            self.task_label.config(text=task_text)
        else:
            self.task_label.config(text="Ты мой герой! \nЭто было потрясающе!")

    def run(self):
        self.root.mainloop()
