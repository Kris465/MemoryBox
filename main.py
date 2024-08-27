from tkinter import Tk
from loguru import logger
from menu_class import UserMenu


def main():
    ''' Формат даты = "2024-08-19" '''

    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation='3 days', backtrace=True, diagnose=True)

    root = Tk()
    user_menu = UserMenu(root)
    root.wait_window()  # Ожидаем закрытия окна
    data_dict = user_menu.get_data()  # Получаем данные после закрытия окна

    print(data_dict)  # Печатаем полученные данные


if __name__ == '__main__':
    main()
