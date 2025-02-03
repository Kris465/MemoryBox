import tkinter as tk
from tkinter import PhotoImage, messagebox


def validate_data(data):
    if not data["chapter"].isdigit():
        return "Поле 'chapter/from' должно быть числом"
    if not data["title"]:
        return "Поле 'Title' не может быть пустым"
    if not data["link"]:
        return "Поле 'Link' не может быть пустым"
    return None


def on_submit(root, mode_var, chapter_entry, title_entry, link_entry):
    data = {
        "mode": mode_var.get(),
        "chapter": chapter_entry.get(),
        "title": title_entry.get(),
        "link": link_entry.get()
    }

    error_message = validate_data(data)
    if error_message:
        messagebox.showerror("Ошибка", error_message)
        return None

    root.quit()
    return data


def create_interface():
    root = tk.Tk()
    root.title("Hellhound Interface")
    root.geometry("500x300")
    icon = PhotoImage(file="yin.png")
    root.iconphoto(False, icon)

    mode_var = tk.StringVar(value="stepper")
    tk.Label(root, text="Выберите режим:").grid(row=0, column=0,
                                                padx=10, pady=10, sticky="w")

    stepper_rb = tk.Radiobutton(root, text="Stepper",
                                variable=mode_var, value="stepper")
    collector_rb = tk.Radiobutton(root, text="Collector",
                                  variable=mode_var, value="collector")
    one_chapter_rb = tk.Radiobutton(root, text="One Chapter",
                                    variable=mode_var, value="one_chapter")

    stepper_rb.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    collector_rb.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    one_chapter_rb.grid(row=3, column=0, padx=10, pady=5, sticky="w")

    tk.Label(root, text="chapter/from:").grid(row=1, column=1,
                                              padx=10, pady=5, sticky="e")
    chapter_entry = tk.Entry(root)
    chapter_entry.grid(row=1, column=2, padx=10, pady=5)

    tk.Label(root, text="Title:").grid(row=4, column=0, padx=10,
                                       pady=5, sticky="w")
    title_entry = tk.Entry(root, width=40)
    title_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

    tk.Label(root, text="Link:").grid(row=5, column=0, padx=10,
                                      pady=5, sticky="w")
    link_entry = tk.Entry(root, width=40)
    link_entry.grid(row=5, column=1, columnspan=2, padx=10, pady=5)

    submit_button = tk.Button(root, text="Submit", command=lambda: on_submit(
        root, mode_var, chapter_entry, title_entry, link_entry))
    submit_button.grid(row=6, column=0, columnspan=3, pady=20)

    root.mainloop()

    return on_submit(root, mode_var, chapter_entry, title_entry, link_entry)
