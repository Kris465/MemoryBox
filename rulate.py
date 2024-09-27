from loguru import logger
from selenium import webdriver


class RulateScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_rulate(self):
        try:
            logger.info("Открытие сайта rulate")
            self.driver.get("https://tl.rulate.ru/collection")
            logger.info("Сайт rulate открыт успешно")
        except Exception as e:
            logger.error(f"Ошибка при открытии сайта: {e}")

    def close(self):
        logger.info("Закрытие веб-драйвера")
        self.driver.quit()
