from loguru import logger
from selenium import webdriver


class OzonScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_ozon(self):
        try:
            logger.info("Открытие сайта Ozon")
            self.driver.get("https://www.ozon.ru")
            logger.info("Сайт Ozon открыт успешно")
        except Exception as e:
            logger.error(f"Ошибка при открытии сайта: {e}")

    def close(self):
        logger.info("Закрытие веб-драйвера")
        self.driver.quit()
