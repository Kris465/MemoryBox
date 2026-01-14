from datetime import date, timedelta
from typing import List, Optional
from loguru import logger
from timetable.db_entity import DBEntity


class TimetableManager:
    """
    Менеджер для управления памятными датами
    """

    def __init__(self, db_entity: DBEntity):
        self.db_entity = db_entity
    
    def add_memorable_date(self, name: str, date: date, description: str = None, category: str = None) -> int:
        """Добавление новой памятной даты"""
        logger.info(f"Добавление памятной даты через менеджер: {name}, {date}")
        try:
            result = self.db_entity.add_memorable_date(name, date, description, category)
            logger.info(f"Памятная дата {name} успешно добавлена с ID {result}")
            return result
        except Exception as e:
            logger.error(f"Ошибка при добавлении памятной даты {name}: {e}")
            raise
    
    def get_memorable_dates_by_month(self, month: int) -> List[tuple]:
        """Получение всех памятных дат в заданном месяце"""
        logger.info(f"Получение памятных дат за месяц: {month}")
        try:
            result = self.db_entity.get_memorable_dates_by_month(month)
            logger.info(f"Получено {len(result)} памятных дат за месяц {month}")
            return result
        except Exception as e:
            logger.error(f"Ошибка при получении памятных дат за месяц {month}: {e}")
            raise

    def get_memorable_date_by_id(self, date_id: int) -> Optional[tuple]:
        """Получение памятной даты по ID"""
        logger.info(f"Получение памятной даты по ID: {date_id}")
        try:
            result = self.db_entity.get_memorable_date_by_id(date_id)
            if result:
                logger.info(f"Памятная дата с ID {date_id} найдена")
            else:
                logger.info(f"Памятная дата с ID {date_id} не найдена")
            return result
        except Exception as e:
            logger.error(f"Ошибка при получении памятной даты с ID {date_id}: {e}")
            raise

    def get_all_memorable_dates(self) -> List[tuple]:
        """Получение всех памятных дат"""
        logger.info("Получение всех памятных дат")
        try:
            result = self.db_entity.get_all_memorable_dates()
            logger.info(f"Получено {len(result)} памятных дат")
            return result
        except Exception as e:
            logger.error(f"Ошибка при получении всех памятных дат: {e}")
            raise

    def update_memorable_date(self, date_id: int, name: str = None, date_val: date = None,
                             description: str = None, category: str = None):
        """Обновление памятной даты"""
        logger.info(f"Обновление памятной даты с ID: {date_id}")
        try:
            self.db_entity.update_memorable_date(date_id, name, date_val, description, category)
            logger.info(f"Памятная дата с ID {date_id} обновлена")
        except Exception as e:
            logger.error(f"Ошибка при обновлении памятной даты с ID {date_id}: {e}")
            raise

    def delete_memorable_date(self, date_id: int):
        """Удаление памятной даты"""
        logger.info(f"Удаление памятной даты с ID: {date_id}")
        try:
            self.db_entity.delete_memorable_date(date_id)
            logger.info(f"Памятная дата с ID {date_id} удалена")
        except Exception as e:
            logger.error(f"Ошибка при удалении памятной даты с ID {date_id}: {e}")
            raise
    
    def get_upcoming_dates(self, days_ahead: int = 7) -> List[tuple]:
        """Получение предстоящих памятных дат в ближайшие days_ahead дней"""
        logger.info(f"Получение предстоящих памятных дат за {days_ahead} дней")
        try:
            all_dates = self.db_entity.get_all_memorable_dates()
            upcoming_dates = []

            today = date.today()
            future_date = today + timedelta(days=days_ahead)

            for record in all_dates:
                _, name, record_date_str, description, category, created_at = record
                record_date = date.fromisoformat(record_date_str)

                # Создаем дату в текущем году
                current_year_date = date(today.year, record_date.month, record_date.day)

                # Если дата уже прошла в этом году, смотрим следующий год
                if current_year_date < today:
                    current_year_date = date(today.year + 1, record_date.month, record_date.day)

                # Проверяем, попадает ли дата в диапазон
                if today <= current_year_date <= future_date:
                    upcoming_dates.append((record[0], name, current_year_date.isoformat(), description, category))

            logger.info(f"Найдено {len(upcoming_dates)} предстоящих памятных дат за {days_ahead} дней")
            return upcoming_dates
        except Exception as e:
            logger.error(f"Ошибка при получении предстоящих памятных дат: {e}")
            raise

    def calculate_age_or_anniversary(self, date_id: int) -> Optional[int]:
        """Вычисление возраста или юбилея для памятной даты"""
        logger.info(f"Вычисление возраста или юбилея для памятной даты с ID: {date_id}")
        try:
            record = self.db_entity.get_memorable_date_by_id(date_id)
            if not record:
                logger.info(f"Памятная дата с ID {date_id} не найдена")
                return None

            _, _, record_date_str, _, _, created_at = record
            birth_date = date.fromisoformat(record_date_str)

            today = date.today()
            age = today.year - birth_date.year

            # Если день рождения еще не наступил в этом году, уменьшаем возраст на 1
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1

            logger.info(f"Для памятной даты с ID {date_id} вычислен возраст/юбилей: {age}")
            return age
        except Exception as e:
            logger.error(f"Ошибка при вычислении возраста или юбилея для памятной даты с ID {date_id}: {e}")
            raise