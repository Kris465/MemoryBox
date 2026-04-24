from datetime import date
from typing import List, Optional
from loguru import logger
from timetable.db_entity import DBEntity


class ReminderEntity:
    """
    Сущность для управления напоминаниями
    """

    def __init__(self, db_entity: DBEntity):
        self.db_entity = db_entity

    def add_reminder_record(self, date_id: int, is_active: bool = True):
        """Добавление записи в историю напоминаний"""
        logger.info(f"Добавление записи в историю напоминаний для даты с ID {date_id}, is_active={is_active}")
        try:
            self.db_entity.add_reminder_record(date_id, is_active)
            logger.info(f"Запись в историю напоминаний для даты с ID {date_id} добавлена")
        except Exception as e:
            logger.error(f"Ошибка при добавлении записи в историю напоминаний для даты с ID {date_id}: {e}")
            raise

    def get_reminder_records(self, date_id: int = None) -> List[tuple]:
        """Получение записей из истории напоминаний"""
        logger.info(f"Получение записей из истории напоминаний для даты с ID {date_id}" if date_id else "Получение всех записей из истории напоминаний")
        try:
            result = self.db_entity.get_reminder_records(date_id)
            logger.info(f"Получено {len(result)} записей из истории напоминаний для даты с ID {date_id}" if date_id else f"Получено {len(result)} записей из истории напоминаний")
            return result
        except Exception as e:
            logger.error(f"Ошибка при получении записей из истории напоминаний для даты с ID {date_id}: {e}" if date_id else f"Ошибка при получении всех записей из истории напоминаний: {e}")
            raise

    def mark_as_congratulated(self, date_id: int):
        """Отметить памятную дату как поздравленную"""
        logger.info(f"Отметка памятной даты с ID {date_id} как поздравленной")
        try:
            self.add_reminder_record(date_id, is_active=False)
            logger.info(f"Памятная дата с ID {date_id} отмечена как поздравленная")
        except Exception as e:
            logger.error(f"Ошибка при отметке памятной даты с ID {date_id} как поздравленной: {e}")
            raise

    def was_congratulated_today(self, date_id: int) -> bool:
        """Проверить, было ли сегодня поздравление для указанной даты"""
        logger.info(f"Проверка, было ли сегодня поздравление для даты с ID {date_id}")
        try:
            records = self.get_reminder_records(date_id)
            if not records:
                logger.info(f"Для даты с ID {date_id} нет записей в истории напоминаний")
                return False

            # Берем последнюю запись
            latest_record = records[0]
            _, _, is_active, created_at = latest_record

            # Проверяем, была ли запись сегодня и была ли она неактивной (поздравленной)
            record_date = date.fromisoformat(created_at.split()[0])
            today = date.today()

            result = record_date == today and not is_active
            logger.info(f"Для даты с ID {date_id} {'было' if result else 'не было'} сегодня поздравление")
            return result
        except Exception as e:
            logger.error(f"Ошибка при проверке поздравления сегодня для даты с ID {date_id}: {e}")
            raise
