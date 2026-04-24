import asyncio
from loguru import logger
from bot import UniversityTelegramBot


async def main():
    """Основная функция приложения"""

    logger.add(
        "university_bot.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} | {message}",
        level="INFO",
        rotation="10 MB",
        retention="30 days"
    )

    logger.info("Запуск University Bot...")
    bot = UniversityTelegramBot()
    await bot.run()


if __name__ == "__main__":
    asyncio.run(main())
