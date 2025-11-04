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
            # Импорты внутри метода
            from parser import UniversityParser
            from scheduler import ScheduleChecker

            checker = ScheduleChecker()

            async with UniversityParser(headless=True,
                                        use_saved_session=True) as parser:
                result = await parser.get_schedule_for_date(target_date)
                message_text = checker.format_telegram_message(result)

                await message.answer(message_text,
                                     parse_mode=ParseMode.MARKDOWN)

        except Exception as e:
            logger.error(f"Ошибка при запросе расписания: {e}")
            await message.answer("Не удалось получить расписание")

    async def handle_private_message(self, message: Message):
        """Обработка приватных сообщений"""
        if message.chat.type == 'private':
            await message.answer(
                "Эх... Это приватный чат...\n\n"
                "Я не способен общаться тет-а-тет"
            )
            logger.warning(
                f"Блокировка приватного сообщения от {message.from_user.id}")

    async def handle_non_command_message(self, message: Message):
        """Обработка некомандных сообщений в разрешенной группе"""
        if (
            message.chat.type in ['group', 'supergroup']
            and message.chat.id == ALLOWED_GROUP_ID
        ):
            if not message.text.startswith('/'):
                await message.answer(
                    "Я реагирую только на команды. Пожалуйста, "
                    "используйте команды для взаимодействия со мной."
                )
                logger.warning(
                    f"Блокировка некомандного сообщения в разрешенной "
                    f"группе {message.chat.id}"
                )

    async def handle_other_group_messages(self, message: Message):
        """Обработка сообщений из других групповых чатов"""
        if (
            message.chat.type in ['group', 'supergroup']
            and message.chat.id != ALLOWED_GROUP_ID
        ):
            await message.answer(
                "И как меня сюда занесло?!\n\n"
                "Смысл моего существования не подразумевает работу "
                "в этом чате"
            )
            logger.warning(
                f"Блокировка сообщения из чужого чата {message.chat.id}"
            )

    async def _is_allowed_chat(self, message: Message) -> bool:
        """Проверяем, разрешен ли этот чат"""
        if message.chat.id != ALLOWED_GROUP_ID:
            if message.chat.type == 'private':
                await self.handle_private_message(message)
            else:
                await self.handle_other_group_messages(message)
            return False
        return True

    def setup_handlers(self):
        """Настраиваем обработчики команд"""
        router.message.register(self.start,
                                Command(commands=['start', 'help']))
        router.message.register(self.get_schedule_today,
                                Command(commands=['schedule', 'rasp']))

        # Handle private messages
        router.message.register(self.handle_private_message,
                                F.chat.type == 'private')

        # Handle non-command messages in allowed group
        router.message.register(
            self.handle_non_command_message,
            F.chat.type.in_(['group', 'supergroup']) & (F.chat.id == ALLOWED_GROUP_ID) & ~F.text.startswith('/')
        )

        # Handle messages in other groups
        router.message.register(
            self.handle_other_group_messages,
            F.chat.type.in_(['group', 'supergroup']) & (F.chat.id != ALLOWED_GROUP_ID)
        )

    async def send_daily_schedule(self):
        """Ежедневная отправка расписания (вызывается планировщиком)"""
        try:
            from parser import UniversityParser
            from scheduler import ScheduleChecker

            checker = ScheduleChecker()

            async with UniversityParser(headless=True,
                                        use_saved_session=True) as parser:
                result = await parser.get_schedule_for_date()
                message_text = checker.format_telegram_message(result)

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
                logger.error(
                    f"Не удалось отправить сообщение об ошибке: {send_error}"
                )

    def setup_scheduler(self):
        """Настройка планировщика для ежедневной отправки"""
        # Ежедневно в 11:00
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
