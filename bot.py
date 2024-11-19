from loguru import logger


class Bot:
    def __init__(self, session):
        self.novels = []
        self.session = session

    def get_all_novels(self):
        logger.info("Вызван метод get_all_novels у объекта бота")
