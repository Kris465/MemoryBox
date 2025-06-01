from aiogram import Router, types
from aiogram.filters import Command
from aiogram import Bot
from loguru import logger

from bot.services import get_news

from .observer import NewsSubject, UserObserver


def setup_handlers(dp: Router, news_subject: NewsSubject, bot: Bot) -> None:
    router = Router()
    dp.include_router(router)

    @router.message(Command('start'))
    async def start(message: types.Message):
        observer = UserObserver(message.from_user.id, bot)
        news_subject.attach(observer)

        try:
            initial_news = get_news(limit=5)
            if initial_news:
                await message.answer("Вот последние новости:")
                for item in initial_news:
                    await bot.send_message(
                        message.from_user.id,
                        f"{item['title']}\n{item['url']}",
                        disable_web_page_preview=True
                    )
            else:
                await message.answer("Пока нет доступных новостей.")
        except Exception as e:
            logger.error(f"Ошибка при отправке начальных новостей: {e}")
            await message.answer("Не удалось загрузить начальные новости.")

        await message.answer("Вы подписались на автоматические уведомления о новых новостях!")

    @router.message(Command('stop'))
    async def stop(message: types.Message):
        observer = UserObserver(message.from_user.id, bot)
        news_subject.detach(observer)
        await message.answer("Вы отписались от новостей.")
