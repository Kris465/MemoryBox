import tkinter as tk
from tkinter import messagebox


def create_interface():
    def on_submit():

        data = {
            "mode": mode_var.get(),
            "chapter": chapter_entry.get(),
            "title": title_entry.get(),
            "link": link_entry.get()
        }

        if not data["chapter"].isdigit():
            messagebox.showerror("Ошибка",
                                 "Поле 'chapter/from' должно быть числом")
            return
        if not data["title"]:
            messagebox.showerror("Ошибка", "Поле 'Title' не может быть пустым")
            return
        if not data["link"]:
            messagebox.showerror("Ошибка", "Поле 'Link' не может быть пустым")
            return

        root.quit()
        root.destroy()
        return data

    root = tk.Tk()
    root.title("Hellhound Interface")
    root.geometry("400x300")

    logo_label = tk.Label(root, text="LOGO", font=("Arial", 16))
    logo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    app_name_label = tk.Label(root, text="Hellhound", font=("Arial", 20))
    app_name_label.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

    mode_var = tk.StringVar(value="stepper")
    stepper_rb = tk.Radiobutton(root, text="Stepper",
                                variable=mode_var, value="stepper")
    collector_rb = tk.Radiobutton(root, text="Collector",
                                  variable=mode_var, value="collector")
    one_chapter_rb = tk.Radiobutton(root, text="One Chapter",
                                    variable=mode_var, value="one_chapter")

    stepper_rb.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    collector_rb.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    one_chapter_rb.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    chapter_label = tk.Label(root, text="chapter/from")
    chapter_label.grid(row=1, column=1, padx=10, pady=5, sticky="e")
    chapter_entry = tk.Entry(root)
    chapter_entry.grid(row=1, column=2, padx=10, pady=5, sticky="w")

    title_label = tk.Label(root, text="Title")
    title_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    title_entry = tk.Entry(root)
    title_entry.grid(row=4, column=1, columnspan=2,
                     padx=10, pady=5, sticky="we")

    link_label = tk.Label(root, text="Link")
    link_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    link_entry = tk.Entry(root)
    link_entry.grid(row=5, column=1, columnspan=2,
                    padx=10, pady=5, sticky="we")

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=6, column=0, columnspan=3, pady=10)

    root.mainloop()

    return on_submit()
