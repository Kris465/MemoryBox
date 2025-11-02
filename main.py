import asyncio
import signal
from loguru import logger
from bot import UniversityTelegramBot


class UniversityBot:
    def __init__(self):
        self.telegram_bot = UniversityTelegramBot()
        self.is_running = True

    def setup_signal_handlers(self):
        """Обработчики сигналов для graceful shutdown"""
        def signal_handler(signum, frame):
            logger.info("Получен сигнал завершения...")
            self.is_running = False

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)


async def run(self):
    """Основной цикл работы бота"""
    logger.info("Запуск University Bot (aiogram 3.x)...")
    self.setup_signal_handlers()

    try:
        await self.telegram_bot.run()
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
    finally:
        logger.info("Бот завершает работу...")
        if hasattr(self.telegram_bot, 'scheduler'):
            self.telegram_bot.scheduler.shutdown()


async def main():
    bot = UniversityBot()
    await bot.run()


if __name__ == "__main__":
    asyncio.run(main())
