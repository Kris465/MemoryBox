from timetable.db_entity import DBEntity
from timetable.manager import TimetableManager
from timetable.housework_manager import HouseworkManager
from reminders.entity import ReminderEntity
from reminders.manager import ReminderManager
from loguru import logger


class CoreManager:
    """
    Управляющий менеджер для всех сущностей проекта
    """

    def __init__(self, db_path: str = "memorable_dates.db"):
        logger.info("Инициализация CoreManager")
        # Инициализация базы данных
        self.db_entity = DBEntity(db_path)

        # Инициализация менеджеров
        self.timetable_manager = TimetableManager(self.db_entity)
        self.housework_manager = HouseworkManager(self.db_entity)
        self.reminder_entity = ReminderEntity(self.db_entity)
        self.reminder_manager = ReminderManager(self.db_entity, self.timetable_manager, self.reminder_entity)

        logger.info("CoreManager успешно инициализирован")

    def get_timetable_manager(self):
        """Получение менеджера расписаний"""
        logger.debug("Получение менеджера расписаний")
        return self.timetable_manager

    def get_housework_manager(self):
        """Получение менеджера домашних дел"""
        logger.debug("Получение менеджера домашних дел")
        return self.housework_manager

    def get_reminder_manager(self):
        """Получение менеджера напоминаний"""
        logger.debug("Получение менеджера напоминаний")
        return self.reminder_manager

    def get_db_entity(self):
        """Получение сущности базы данных"""
        logger.debug("Получение сущности базы данных")
        return self.db_entity