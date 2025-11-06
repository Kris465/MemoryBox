import os
from datetime import datetime
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from dotenv import load_dotenv, find_dotenv
from loguru import logger

load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv('TOKEN')
ALLOWED_GROUP_ID = int(os.getenv('GROUP_ID'))

router = Router()


class UniversityTelegramBot:
    def __init__(self):
        self.bot = None
        self.dp = None
        self.scheduler = AsyncIOScheduler(max_workers=10)

    def format_telegram_message(self, schedule_result: dict) -> str:
        """Форматируем сообщение для Telegram"""
        if not schedule_result.get('success'):
            error_msg = schedule_result.get('error', 'Неизвестная ошибка')
            return f"*Не удалось получить расписание*\n\nОшибка: {error_msg}"

        schedule_data = schedule_result.get('schedule', {})
        date = schedule_result.get('date', 'Неизвестная дата')

        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            formatted_date = date_obj.strftime('%d.%m.%Y')
            weekday = self._get_weekday_russian(date_obj.weekday())
            date_display = f"{formatted_date} ({weekday})"
        except Exception as e:
            logger.warning(f"Ошибка при форматировании даты: {e}")
            date_display = date

        message = f"*Расписание на {date_display}*\n"
        message += f"{schedule_data.get('group_info', 'Группа не определена')}\n\n"

        if not schedule_data.get('has_classes', False):
            if schedule_data.get('next_class_date'):
                message += "*Занятий нет*\n"
                message += f"Ближайшее занятие — {schedule_data['next_class_date']}"
            else:
                message += "*Занятий нет*"
        else:
            message += "*Сегодня есть занятия:*\n\n"

            classes = schedule_data.get('classes', [])
            for i, class_info in enumerate(classes, 1):
                message += f"*{i}. {class_info.get('subject', 'Дисциплина')}*"

                if class_info.get('time'):
                    message += f"{class_info['time']}\n"
                if class_info.get('room'):
                    message += f"{class_info['room']}\n"
                if class_info.get('teacher'):
                    message += f"{class_info['teacher']}\n"

                message += "\n"

        message += f"\n_Обновлено: {datetime.now().strftime('%H:%M')}_"
        return message

    def _get_weekday_russian(self, weekday: int) -> str:
        """Получаем день недели на русском"""
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
                'Пятница', 'Суббота', 'Воскресенье']
        return days[weekday]

    async def _is_allowed_chat(self, message: Message) -> bool:
        """Проверяем, разрешен ли этот чат"""
        return message.chat.id == ALLOWED_GROUP_ID

    async def start(self, message: Message):
        """Обработчик команды /start"""
        if not await self._is_allowed_chat(message):
            return

        welcome_text = (
            "Привет! Я бот для проверки расписания университета.\n\n"
            "Я буду автоматически присылать расписание каждое утро в 11:00.\n"
            "Также вы можете запросить расписание вручную командой /schedule\n"
            "Доступные команды:\n"
            "/schedule - Получить расписание на сегодня\n"
            "/start - Получить описание бота\n"
        )
        await message.answer(welcome_text)

    async def get_schedule_today(self, message: Message):
        """Расписание на сегодня"""
        if not await self._is_allowed_chat(message):
            return

        await message.answer("Запрашиваю расписание на сегодня...")
        await self._send_schedule_message(message, datetime.now())

    async def _send_schedule_message(self, message: Message,
                                     target_date: datetime):
        """Отправка сообщения с расписанием"""
        try:
            from parser import UniversityParser

            async with UniversityParser(headless=True, use_saved_session=True) as parser:
                result = await parser.get_schedule_for_date(target_date)
                message_text = self.format_telegram_message(result)

                await message.answer(message_text,
                                     parse_mode=ParseMode.MARKDOWN)

        except Exception as e:
            logger.error(f"Ошибка при запросе расписания: {e}")
            await message.answer("Не удалось получить расписание")

    async def handle_other_chats(self, message: Message):
        """Игнорируем все сообщения из других чатов"""
        pass

    def setup_handlers(self):
        """Настраиваем обработчики команд ТОЛЬКО для разрешенного чата"""
        # Обработчики команд для разрешенной группы
        router.message.register(
            self.start,
            Command(commands=['start']),
            F.chat.id == ALLOWED_GROUP_ID
        )

        router.message.register(
            self.get_schedule_today,
            Command(commands=['schedule']),
            F.chat.id == ALLOWED_GROUP_ID
        )

        router.message.register(self.handle_other_chats)

    async def send_daily_schedule(self):
        """Ежедневная отправка расписания (вызывается планировщиком)"""
        try:
            from parser import UniversityParser

            async with UniversityParser(headless=True,
                                        use_saved_session=True) as parser:
                result = await parser.get_schedule_for_date()
                message_text = self.format_telegram_message(result)

                await self.bot.send_message(
                    chat_id=ALLOWED_GROUP_ID,
                    text=message_text,
                    parse_mode=ParseMode.MARKDOWN
                )

                logger.info("Ежедневное расписание отправлено")

        except Exception as e:
            logger.error(f"Ошибка при отправке ежедневного расписания: {e}")

            try:
                await self.bot.send_message(
                    chat_id=ALLOWED_GROUP_ID,
                    text=f"Не удалось получить расписание: {str(e)}"
                )
            except Exception as send_error:
                logger.error(f"Не удалось отправить сообщение об ошибке: {send_error}")

    def setup_scheduler(self):
        """Настройка планировщика для ежедневной отправки"""
        self.scheduler.add_job(
            self.send_daily_schedule,
            CronTrigger(hour=11, minute=0),
            id='daily_schedule'
        )

        logger.info("Планировщик настроен на ежедневную отправку в 11:00")

    async def run(self):
        """Запуск бота"""
        self.bot = Bot(
            token=TELEGRAM_TOKEN,
            default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
        )

        self.dp = Dispatcher()
        self.dp.include_router(router)

        self.setup_handlers()
        self.setup_scheduler()
        self.scheduler.start()

        logger.info("Telegram бот запущен (aiogram 3.x)")

        await self.dp.start_polling(self.bot)
