import tkinter as tk
from tkinter import messagebox
import json
import os
import winsound


class ClickerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Кликер-игра PRO")
        self.root.geometry("450x350")

        self.score = 0
        self.click_power = 1
        self.theme = "light"
        self.font_size = 12
        self.achievements = {
            10: False,
            50: False,
            100: False
        }
        self.settings_file = "settings.json"

        self.load_settings()

        self.setup_ui()

    def setup_ui(self):
        self.bg_color = "white" if self.theme == "light" else "#333333"
        self.fg_color = "black" if self.theme == "light" else "white"
        self.btn_color = "lightblue" if self.theme == "light" else "#555555"

        self.root.config(bg=self.bg_color)

        self.score_label = tk.Label(
            self.root,
            text=f"Очки: {self.score}",
            font=("Arial", self.font_size),
            bg=self.bg_color,
            fg=self.fg_color
        )
        self.score_label.pack(pady=20)

        self.click_button = tk.Button(
            self.root,
            text="Кликни меня!",
            command=self.add_score,
            bg=self.btn_color,
            fg=self.fg_color,
            font=("Arial", self.font_size)
        )
        self.click_button.pack(pady=10)

        self.settings_button = tk.Button(
            self.root,
            text="Настройки",
            command=self.open_settings,
            bg=self.btn_color,
            fg=self.fg_color
        )
        self.settings_button.pack(pady=10)

    def add_score(self):
        self.score += self.click_power
        self.score_label.config(text=f"Очки: {self.score}")
        self.play_sound()
        self.check_achievements()

    def play_sound(self):
        try:
            winsound.Beep(1000, 100)  # Частота 1000 Гц, длительность 100 мс
        except:
            pass  # Если winsound не работает (не Windows)

    def check_achievements(self):
        for points, achieved in self.achievements.items():
            if self.score >= points and not achieved:
                self.achievements[points] = True
                messagebox.showinfo("Ачивка!", f"Вы набрали {points} очков!")

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Настройки игры")
        settings_window.geometry("350x300")
        settings_window.config(bg=self.bg_color)

        tk.Label(
            settings_window,
            text="Сила клика:",
            bg=self.bg_color,
            fg=self.fg_color
        ).pack()
        click_power_entry = tk.Entry(settings_window)
        click_power_entry.insert(0, str(self.click_power))
        click_power_entry.pack()

        tk.Label(
            settings_window,
            text="Тема:",
            bg=self.bg_color,
            fg=self.fg_color
        ).pack()
        theme_var = tk.StringVar(value=self.theme)
        tk.Radiobutton(
            settings_window,
            text="Светлая",
            variable=theme_var,
            value="light",
            bg=self.bg_color,
            fg=self.fg_color,
            selectcolor=self.btn_color
        ).pack()
        tk.Radiobutton(
            settings_window,
            text="Тёмная",
            variable=theme_var,
            value="dark",
            bg=self.bg_color,
            fg=self.fg_color,
            selectcolor=self.btn_color
        ).pack()

        tk.Label(
            settings_window,
            text="Размер шрифта:",
            bg=self.bg_color,
            fg=self.fg_color
        ).pack()
        font_size_slider = tk.Scale(
            settings_window,
            from_=10,
            to=20,
            orient="horizontal",
            command=lambda x: self.change_font_size(int(x)),
            bg=self.bg_color,
            fg=self.fg_color
        )
        font_size_slider.set(self.font_size)
        font_size_slider.pack()

        def apply_settings():
            try:
                self.click_power = int(click_power_entry.get())
                self.theme = theme_var.get()
                self.update_theme()
                self.save_settings()
                settings_window.destroy()
            except ValueError:
                messagebox.showerror("Ошибка", "Сила клика должна быть числом!")

        tk.Button(
            settings_window,
            text="Применить",
            command=apply_settings,
            bg=self.btn_color,
            fg=self.fg_color
        ).pack(pady=10)

    def change_font_size(self, size):
        self.font_size = size
        self.click_button.config(font=("Arial", size))

    def update_theme(self):
        self.bg_color = "white" if self.theme == "light" else "#333333"
        self.fg_color = "black" if self.theme == "light" else "white"
        self.btn_color = "lightblue" if self.theme == "light" else "#555555"

        self.root.config(bg=self.bg_color)
        self.score_label.config(bg=self.bg_color, fg=self.fg_color)
        self.click_button.config(bg=self.btn_color, fg=self.fg_color)
        self.settings_button.config(bg=self.btn_color, fg=self.fg_color)

    def save_settings(self):
        settings = {
            "click_power": self.click_power,
            "theme": self.theme,
            "font_size": self.font_size
        }
        with open(self.settings_file, "w") as f:
            json.dump(settings, f)

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                settings = json.load(f)
                self.click_power = settings.get("click_power", 1)
                self.theme = settings.get("theme", "light")
                self.font_size = settings.get("font_size", 12)


if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()