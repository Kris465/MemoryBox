import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime


class UserMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Генерация отчета")

        # Глобальный словарь для хранения данных
        self.report_data = {}

        # Поля для ввода
        tk.Label(master, text="Дата с (YYYY-MM-DD):").grid(row=0, column=0)
        self.entry_date_from = tk.Entry(master)
        self.entry_date_from.grid(row=0, column=1)

        tk.Label(master, text="Дата по (YYYY-MM-DD):").grid(row=1, column=0)
        self.entry_date_to = tk.Entry(master)
        self.entry_date_to.grid(row=1, column=1)

        # Выпадающий список для выбора типа отчета
        self.report_type_var = tk.StringVar(value="Выберите тип отчета")
        tk.Label(master, text="Тип отчета:").grid(row=2, column=0)
        report_type_menu = tk.OptionMenu(master, self.report_type_var,
                                         "Поставки", "Склад", "Заказы",
                                         "Продажи",
                                         "Отчет о продажах по реализации")
        report_type_menu.grid(row=2, column=1)

        # Поле для указания пути сохранения
        tk.Label(master, text="Путь для сохранения:").grid(row=3, column=0)
        self.entry_save_path = tk.Entry(master)
        self.entry_save_path.grid(row=3, column=1)

        # Кнопка для выбора пути сохранения
        tk.Button(master, text="Обзор",
                  command=self.browse_path).grid(row=3, column=2)

        # Кнопка для получения отчета
        tk.Button(master, text="Получить отчет",
                  command=self.get_report).grid(row=4, columnspan=3)

        # Метка для результата
        self.label_result = tk.Label(master, text="")
        self.label_result.grid(row=5, columnspan=3)

    def get_report(self):
        date_from = self.entry_date_from.get()
        date_to = self.entry_date_to.get()
        report_type = self.report_type_var.get()
        save_path = self.entry_save_path.get()

        # Проверка формата дат
        try:
            datetime.strptime(date_from, '%Y-%m-%d')
            datetime.strptime(date_to, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror(
                "Ошибка", "Неверный формат даты. Используйте YYYY-MM-DD.")
            return

        # Проверка выбора типа отчета
        if report_type == "Выберите тип отчета":
            messagebox.showerror("Ошибка", "Пожалуйста, выберите тип отчета.")
            return

        # Проверка пути для сохранения
        if not save_path:
            messagebox.showerror("Ошибка",
                                 "Пожалуйста, укажите путь для сохранения.")
            return

        # Обновляем глобальный словарь
        self.report_data = {
            "date_from": date_from,
            "date_to": date_to,
            "report_type": report_type,
            "save_path": save_path
        }

        # Изменение текста в окне
        self.label_result.config(text="Проверьте отчет в папке назначения.")
        # Закрываем окно после получения данных
        self.master.destroy()

    def browse_path(self):
        folder_selected = filedialog.askdirectory()
        self.entry_save_path.delete(0, tk.END)
        self.entry_save_path.insert(0, folder_selected)

    def get_data(self):
        return self.report_data
