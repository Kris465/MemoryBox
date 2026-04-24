from datetime import date, timedelta
from typing import List, Tuple
from loguru import logger
from timetable.db_entity import DBEntity
from timetable.manager import TimetableManager
from reminders.entity import ReminderEntity


class ReminderManager:
    """
    Менеджер для управления напоминаниями о памятных датах
    """

    def __init__(self, db_entity: DBEntity, timetable_manager: TimetableManager, reminder_entity: ReminderEntity):
        self.db_entity = db_entity
        self.timetable_manager = timetable_manager
        self.reminder_entity = reminder_entity

    def check_daily_reminders(self) -> List[Tuple]:
        """
        Проверка и получение списка памятных дат,
        которые приходятся на сегодня или ближайшие дни
        """
        logger.info("Проверка ежедневных напоминаний")
        try:
            all_dates = self.timetable_manager.get_all_memorable_dates()
            today = date.today()
            reminder_list = []

            for record in all_dates:
                date_id, name, record_date_str, description, category, created_at = record
                record_date = date.fromisoformat(record_date_str)

                # Создаем дату в текущем году
                current_year_date = date(today.year, record_date.month, record_date.day)

                # Если дата уже прошла в этом году, смотрим следующий год
                if current_year_date < today:
                    current_year_date = date(today.year + 1, record_date.month, record_date.day)

                # Проверяем, является ли сегодня дата или близка к ней
                days_diff = (current_year_date - today).days

                # Отправляем напоминания в начале месяца, за 7 дней и за 3 дня до события
                if days_diff in [30, 7, 3, 0]:  # В начале месяца (примерно), за неделю, за 3 дня и в день
                    # Проверяем, не было ли уже поздравления сегодня
                    if not self.reminder_entity.was_congratulated_today(date_id):
                        age_or_anniversary = self.timetable_manager.calculate_age_or_anniversary(date_id)

                        # Определяем тип напоминания
                        if days_diff == 30:
                            reminder_type = "monthly"
                        elif days_diff == 7:
                            reminder_type = "week_before"
                        elif days_diff == 3:
                            reminder_type = "three_days_before"
                        else:  # days_diff == 0
                            reminder_type = "on_date"

                        reminder_list.append((date_id, name, current_year_date, description, category, days_diff, age_or_anniversary, reminder_type))

            logger.info(f"Найдено {len(reminder_list)} ежедневных напоминаний")
            return reminder_list
        except Exception as e:
            logger.error(f"Ошибка при проверке ежедневных напоминаний: {e}")
            raise

    def check_monthly_reminders(self) -> List[Tuple]:
        """
        Проверка и получение списка памятных дат,
        которые приходятся на начало месяца
        """
        logger.info("Проверка ежемесячных напоминаний")
        try:
            all_dates = self.timetable_manager.get_all_memorable_dates()
            today = date.today()
            reminder_list = []

            # Проверяем, первое ли это число месяца
            if today.day != 1:
                logger.info("Сегодня не первое число месяца, пропускаем ежемесячные напоминания")
                return reminder_list

            for record in all_dates:
                date_id, name, record_date_str, description, category, created_at = record
                record_date = date.fromisoformat(record_date_str)

                # Создаем дату в текущем году
                current_year_date = date(today.year, record_date.month, record_date.day)

                # Если дата уже прошла в этом году, смотрим следующий год
                if current_year_date < today:
                    current_year_date = date(today.year + 1, record_date.month, record_date.day)

                # Проверяем, в этом ли месяце событие
                if current_year_date.month == today.month:
                    # Проверяем, не было ли уже поздравления сегодня
                    if not self.reminder_entity.was_congratulated_today(date_id):
                        age_or_anniversary = self.timetable_manager.calculate_age_or_anniversary(date_id)
                        reminder_list.append((date_id, name, current_year_date, description, category, 30, age_or_anniversary, "monthly"))

            logger.info(f"Найдено {len(reminder_list)} ежемесячных напоминаний")
            return reminder_list
        except Exception as e:
            logger.error(f"Ошибка при проверке ежемесячных напоминаний: {e}")
            raise

    def mark_as_congratulated(self, date_id: int):
        """Отметить памятную дату как поздравленную"""
        logger.info(f"Отметка памятной даты с ID {date_id} как поздравленной через менеджер")
        try:
            self.reminder_entity.mark_as_congratulated(date_id)
            logger.info(f"Памятная дата с ID {date_id} отмечена как поздравленная")
        except Exception as e:
            logger.error(f"Ошибка при отметке памятной даты с ID {date_id} как поздравленной: {e}")
            raise

    def get_congratulation_message(self, name: str, category: str, age_or_anniversary: int = None) -> str:
        """Генерация сообщения для поздравления"""
        logger.info(f"Генерация сообщения для поздравления: {name}, категория: {category}")
        try:
            if category.lower() == 'birthday':
                if age_or_anniversary is not None:
                    message = f"С днём рождения, {name}! Ему/ей исполняется {age_or_anniversary} лет!"
                else:
                    message = f"С днём рождения, {name}!"
            elif category.lower() == 'anniversary':
                if age_or_anniversary is not None:
                    message = f"Поздравляем с юбилеем, {name}! Прошло {age_or_anniversary} лет!"
                else:
                    message = f"Поздравляем с годовщиной, {name}!"
            else:
                message = f"Не забудьте о важном событии: {name}!"

            logger.info(f"Сгенерировано сообщение для поздравления: {message}")
            return message
        except Exception as e:
            logger.error(f"Ошибка при генерации сообщения для поздравления {name}: {e}")
            raise

    def get_monthly_summary(self, month: int = None) -> List[Tuple]:
        """Получение сводки по памятным датам в месяце"""
        if month is None:
            month = date.today().month

        logger.info(f"Получение сводки по памятным датам за месяц: {month}")
        try:
            result = self.timetable_manager.get_memorable_dates_by_month(month)
            logger.info(f"Получено {len(result)} памятных дат за месяц {month}")
            return result
        except Exception as e:
            logger.error(f"Ошибка при получении сводки по памятным датам за месяц {month}: {e}")
            raise