from loguru import logger
from rulate import RulateScraper


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    rulate_scraper = RulateScraper()
    rulate_scraper.open_rulate()
    input("Нажмите Enter для закрытия веб-драйвера...")
    rulate_scraper.close()


if __name__ == "__main__":
    main()
