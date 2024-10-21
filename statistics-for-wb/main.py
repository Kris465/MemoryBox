from tkinter import Tk
from loguru import logger
from menu_class import UserMenu
from wb_api import WbApi


def main():
    ''' Формат даты = "2024-08-19" '''

    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation='3 days', backtrace=True, diagnose=True)

    root = Tk()
    user_menu = UserMenu(root)
    root.wait_window()  # Ожидаем закрытия окна
    data_dict = user_menu.get_data()  # Получаем данные после закрытия окна
    logger.info(data_dict)

    '''
    Вид получаемых данных из меню:
            self.report_data = {
            "date_from": date_from,
            "date_to": date_to,
            "report_type": report_type,
            "save_path": save_path
        }
    '''

    wb_api = WbApi(data_dict)
    wb_api.logic()


if __name__ == '__main__':
    main()
