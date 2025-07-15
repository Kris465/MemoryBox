import asyncio
import os

from aiogram import Bot, Dispatcher
from loguru import logger
from dotenv import load_dotenv, find_dotenv

from checker import Checker

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
bot = Bot(token=TOKEN)
dp = Dispatcher()
checker = Checker(link="https://sleepytranslations.com/series/please-be-quiet-and-take-off-your-something/chapter-1/")


async def send_check_results():
    try:
        results = checker.parse()

        if results:
            message_text = "🔔 Результаты проверки:\n\n" + "\n".join(str(item) for item in results)
            await bot.send_message(chat_id=CHANNEL_ID, text=message_text)
            logger.success("Результаты отправлены в канал")
        else:
            await bot.send_message(chat_id=CHANNEL_ID, text="ℹ На данный момент изменений нет")
            logger.info("Новых изменений не обнаружено")

    except Exception as e:
        error_msg = f"Ошибка при проверке: {str(e)}"
        await bot.send_message(chat_id=CHANNEL_ID, text=error_msg)
        logger.error(f"Ошибка: {e}")


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)

    logger.info("Запуск бота")

    asyncio.create_task(periodic_check(interval=3600))

    await dp.start_polling(bot)


async def periodic_check(interval: int):
    """Функция для периодической проверки"""
    while True:
        await send_check_results()
        await asyncio.sleep(interval)


if __name__ == '__main__':
    asyncio.run(main())
