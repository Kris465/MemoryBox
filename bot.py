import os
from datetime import datetime
from typing import Optional

from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from parser import UniversityParser, update_schedule_daily
from json_tools import ScheduleJsonTools
from dotenv import load_dotenv, find_dotenv
from loguru import logger

load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv('TOKEN')
ALLOWED_GROUP_ID = int(os.getenv('GROUP_ID'))

router = Router()


class UniversityTelegramBot:
    """Telegram бот для работы с расписанием университета"""

    def __init__(self):
        self.bot: Optional[Bot] = None
        self.dp: Optional[Dispatcher] = None
        self.scheduler = AsyncIOScheduler()
        self.json_tools = ScheduleJsonTools()
        self.parser = UniversityParser()

    async def shutdown(self):
        """Корректное завершение работы бота"""
        logger.info("Завершение работы Telegram бота...")

        if self.scheduler.running:
            self.scheduler.shutdown(wait=False)

        if self.dp:
            await self.dp.storage.close()
            await self.dp.storage.wait_closed()

        if self.bot:
            await self.bot.session.close()

    def format_telegram_message(self, schedule_result: dict) -> str:
        """Форматирование сообщения для Telegram"""
        if not schedule_result.get('success'):
            error_msg = schedule_result.get('error', 'Неизвестная ошибка')
            return f"*Не удалось получить расписание*\n\nОшибка: {error_msg}"

        schedule_data = schedule_result.get('schedule', {})
        date = schedule_result.get('date', 'Неизвестная дата')

        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            formatted_date = date_obj.strftime('%d.%m.%Y')
            days = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
                    'Пятница', 'Суббота', 'Воскресенье']
            weekday = days[date_obj.weekday()]
            date_display = f"{formatted_date} ({weekday})"
        except Exception as e:
            logger.warning(f"Ошибка форматирования даты: {e}")
            date_display = date

        message_parts = [f"*Расписание на {date_display}*"]

        if group_info := schedule_data.get('group_info'):
            message_parts.append(f"*Группа:* {group_info}")

        message_parts.append("")

        if not schedule_data.get('has_classes', False):
            if next_class_date := schedule_data.get('next_class_date'):
                message_parts.extend([
                    "*Занятий нет*",
                    f"*Ближайшее занятие:* {next_class_date}"
                ])
            else:
                message_parts.append("*Занятий нет*")
        else:
            message_parts.append("*Сегодня есть занятия:*\n")

            classes = schedule_data.get('classes', [])
            for i, class_info in enumerate(classes, 1):
                class_parts = [f"*{i}. {class_info.get('subject', 'Дисциплина')}*"]

                if time := class_info.get('time'):
                    class_parts.append(f"{time}")
                if room := class_info.get('room'):
                    class_parts.append(f"{room}")
                if teacher := class_info.get('teacher'):
                    class_parts.append(f"{teacher}")

                message_parts.append("\n".join(class_parts))

        message_parts.append(f"Обновлено: {datetime.now().strftime('%H:%M')}")

        return "\n".join(message_parts)

    async def start_command(self, message: Message):
        """Обработчик команды /start только для разрешенной группы"""
        welcome_text = (
            "Привет! Я бот для проверки расписания университета.\n\n"
            "*Доступные команды:*\n"
            "/schedule - Получить расписание на сегодня\n"
            "/start - Описание бота\n\n"
            "*Автоматические уведомления:*\n"
            "Расписание приходит каждый день в 8:00"
        )
        await message.answer(welcome_text, parse_mode=ParseMode.MARKDOWN)

    async def schedule_command(self, message: Message):
        """Обработчик команды /schedule только для разрешенной группы"""
        await message.answer("Смотрю расписание на сегодня...")

        # Если файла нет - парсим
        if not self.json_tools.file_exists():
            await message.answer(
                "Файл с расписанием не найден. Схожу узнаю...")
            success = await self.parser.parse_and_save_schedule()
            if not success:
                await message.answer(
                    "Не удалось получить расписание. Поcмотрю позже.")
                return

        # Получаем расписание из JSON
        result = self.json_tools.get_schedule_for_date(datetime.now())
        message_text = self.format_telegram_message(result)
        await message.answer(message_text, parse_mode=ParseMode.MARKDOWN)

    def setup_handlers(self):
        """Настройка обработчиков команд"""
        router.message.register(
            self.start_command,
            Command(commands=['start']),
            F.chat.id == ALLOWED_GROUP_ID
        )

        router.message.register(
            self.schedule_command,
            Command(commands=['schedule']),
            F.chat.id == ALLOWED_GROUP_ID
        )

    async def send_daily_schedule(self):
        """Ежедневная отправка расписания"""
        try:
            logger.info("Обновление ежедневного расписания...")

            # Обновляем данные
            update_success = await update_schedule_daily()
            if not update_success:
                logger.warning(
                    "Не могу обновить расписание, посмотрю, что есть текущее")

            # Получаем расписание
            result = self.json_tools.get_schedule_for_date(datetime.now())
            message_text = self.format_telegram_message(result)

            await self.bot.send_message(
                chat_id=ALLOWED_GROUP_ID,
                text=message_text,
                parse_mode=ParseMode.MARKDOWN
            )

            logger.info("Ежедневное расписание отправлено")

        except Exception as e:
            logger.error(f"Ошибка при отправке ежедневного расписания: {e}")

    def setup_scheduler(self):
        """Настройка планировщика для ежедневной отправки"""
        self.scheduler.add_job(
            self.send_daily_schedule,
            CronTrigger(hour=8, minute=0),
            id='daily_schedule'
        )
        logger.info("Планировщик настроен на ежедневную отправку в 8:00")

    async def run(self):
        """Запуск бота"""
        try:
            self.bot = Bot(
                token=TELEGRAM_TOKEN,
                default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
            )

            self.dp = Dispatcher()
            self.dp.include_router(router)

            self.setup_handlers()
            self.setup_scheduler()

            self.scheduler.start()
            logger.info("Telegram бот запущен")

            await self.dp.start_polling(self.bot)

        except Exception as e:
            logger.error(f"Ошибка при запуске бота: {e}")
            raise
