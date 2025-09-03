from aiogram import Bot
from typing import Set

from loguru import logger


class NewsSubject:
    def __init__(self):
        self._observers: Set[UserObserver] = set()
        self._last_news = []

    def attach(self, observer: 'UserObserver'):
        self._observers.add(observer)
        logger.info(f"Подписчик добавлен: {observer.user_id}")

    def detach(self, observer: 'UserObserver'):
        self._observers.discard(observer)
        logger.info(f"Подписчик отписан: {observer.user_id}")

    async def notify(self, news: list):
        logger.info(f"Рассылаю новости {len(news)} подписчикам")
        if not self._observers:
            logger.warning("Нет подписчиков для рассылки")
        for observer in self._observers:
            logger.debug(f"Отправляю новости пользователю {observer.user_id}")
            await observer.update(news)


class UserObserver:
    def __init__(self, user_id: int, bot: Bot):
        self.user_id = user_id
        self.bot = bot

    async def update(self, news: list):
        for item in news:
            await self.bot.send_message(
                self.user_id,
                f"Новая новость: {item['title']}\n{item['url']}"
            )
