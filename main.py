from loguru import logger
from wb_api import WbApi


def main():
    ''' Формат даты = "2024-08-19" '''

    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation='3 days', backtrace=True, diagnose=True)

    print("Hello")
    date = input("Введите дату (YYYY-MM-DD): ")
    wb_api = WbApi(date)
    wb_api.get_sales_statistics()


if __name__ == '__main__':
    main()
