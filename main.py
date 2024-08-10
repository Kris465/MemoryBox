from loguru import logger
from ozon import OzonScraper


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    ozon_scraper = OzonScraper()
    ozon_scraper.open_ozon()
    input("Нажмите Enter для закрытия веб-драйвера...")
    ozon_scraper.close()


if __name__ == "__main__":
    main()
