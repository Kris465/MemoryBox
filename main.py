import asyncio
import os
from datetime import datetime

from aiogram import Bot, Dispatcher
from loguru import logger
from dotenv import load_dotenv, find_dotenv

from bot.handlers import setup_handlers
from core.manager import CoreManager


load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def send_daily_reminders(bot: Bot, core_manager):
    """Функция для отправки ежедневных напоминаний"""
    await asyncio.sleep(10)  # Небольшая задержка перед первым запуском

    while True:
        try:
            logger.info("Проверка ежедневных напоминаний запущена")
            # Получаем менеджеры
            reminder_manager = core_manager.get_reminder_manager()
            timetable_manager = core_manager.get_timetable_manager()

            # Проверяем ежедневные напоминания
            daily_reminders = reminder_manager.check_daily_reminders()
            logger.info(f"Найдено {len(daily_reminders)} ежедневных напоминаний")

            # Отправляем напоминания (в реальном боте здесь нужно будет указать ID пользователей)
            for reminder_data in daily_reminders:
                date_id, name, current_year_date, description, category, days_diff, age_or_anniversary, reminder_type = reminder_data

                # В реальном приложении здесь нужно будет отправить сообщение конкретным пользователям
                # Для демонстрации выводим в лог
                if reminder_type == "on_date":
                    message = f"Сегодня {name}! {'Им' if category == 'birthday' else 'Ей'} исполняется {age_or_anniversary} лет!" if age_or_anniversary else f"Сегодня {name}!"
                elif reminder_type == "three_days_before":
                    message = f"Через 3 дня ({current_year_date}) будет {name}!"
                elif reminder_type == "week_before":
                    message = f"Через неделю ({current_year_date}) будет {name}!"
                elif reminder_type == "monthly":
                    message = f"В этом месяце ({current_year_date}) будет {name}!"

                logger.info(f"Напоминание: {message}")

                # Отмечаем, что напоминание было отправлено
                reminder_manager.mark_as_congratulated(date_id)

            # Проверяем ежемесячные напоминания
            monthly_reminders = reminder_manager.check_monthly_reminders()
            logger.info(f"Найдено {len(monthly_reminders)} ежемесячных напоминаний")

            # Объединяем с ежедневными напоминаниями
            all_reminders = daily_reminders + monthly_reminders

            # Здесь в реальном приложении нужно отправить сообщения пользователям
            # Пока просто логируем

        except Exception as e:
            logger.error(f"Ошибка при отправке напоминаний: {e}")

        # Ждем 24 часа перед следующей проверкой
        await asyncio.sleep(24 * 3600)  # 24 часа в секундах


async def main():
    # Setup logging
    logger.add('file.log',
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days")

    if not BOT_TOKEN:
        logger.error("BOT_TOKEN is not set in environment variables")
        return

    # Initialize bot and dispatcher
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Initialize core manager
    core_manager = CoreManager()

    # Setup handlers
    setup_handlers(dp)

    logger.info("Starting bot...")

    # Запускаем задачу отправки напоминаний в фоне
    reminder_task = asyncio.create_task(send_daily_reminders(bot, core_manager))

    try:
        logger.info("Bot polling started")
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error in bot polling: {e}")
    finally:
        logger.info("Cancelling reminder task...")
        reminder_task.cancel()  # Отменяем задачу напоминаний при завершении
        try:
            await reminder_task
        except asyncio.CancelledError:
            logger.info("Reminder task cancelled successfully")
        await bot.session.close()
        logger.info("Bot session closed")


if __name__ == '__main__':
    asyncio.run(main())
