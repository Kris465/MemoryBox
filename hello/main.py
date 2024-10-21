from loguru import logger
from parser import WebParser


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    url = input("Введите адрес сайта: ")
    pars = WebParser(url)
    pars.fetch()

    pars.save_html()
    print(pars.get_status_code())


if __name__ == "__main__":
    main()
