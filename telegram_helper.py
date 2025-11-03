from aiogram.enums import ParseMode
from loguru import logger


async def send_schedule_to_telegram(message: str, bot_instance=None):
    """Функция для отправки сообщения в Telegram"""
    if not hasattr(send_schedule_to_telegram, 'TELEGRAM_TOKEN'):
        from dotenv import load_dotenv, find_dotenv
        import os
        load_dotenv(find_dotenv())
        send_schedule_to_telegram.TELEGRAM_TOKEN = os.getenv('TOKEN')
        send_schedule_to_telegram.ALLOWED_GROUP_ID = int(os.getenv('GROUP_ID'))

    if not send_schedule_to_telegram.TELEGRAM_TOKEN or not send_schedule_to_telegram.ALLOWED_GROUP_ID:
        logger.error("Не настроены TELEGRAM_TOKEN или ALLOWED_GROUP_ID")
        return

    try:
        if bot_instance:
            # Используем существующий экземпляр бота
            await bot_instance.send_message(
                chat_id=send_schedule_to_telegram.ALLOWED_GROUP_ID,
                text=message,
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            # Создаем временный экземпляр только если нужно
            from aiogram import Bot
            bot = Bot(token=send_schedule_to_telegram.TELEGRAM_TOKEN)
            await bot.send_message(
                chat_id=send_schedule_to_telegram.ALLOWED_GROUP_ID,
                text=message,
                parse_mode=ParseMode.MARKDOWN
            )
            await bot.session.close()

        logger.info("Сообщение отправлено в Telegram")
    except Exception as e:
        logger.error(f"Ошибка отправки в Telegram: {e}")
