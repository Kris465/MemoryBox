from datetime import date, timedelta
from typing import List, Optional
from loguru import logger
from timetable.db_entity import DBEntity


class HouseworkManager:
    """
    Менеджер для управления домашними делами
    """

    def __init__(self, db_entity: DBEntity):
        self.db_entity = db_entity
    
    def add_housework_task(self, name: str, duration: int = None, frequency: str = None, last_completed: date = None) -> int:
        """Добавление новой задачи по дому"""
        logger.info(f"Добавление задачи по дому через менеджер: {name}")
        try:
            result = self.db_entity.add_housework_task(name, duration, frequency, last_completed)
            logger.info(f"Задача по дому {name} успешно добавлена с ID {result}")
            return result
        except Exception as e:
            logger.error(f"Ошибка при добавлении задачи по дому {name}: {e}")
            raise
    
    def get_all_housework_tasks(self) -> List[tuple]:
        """Получение всех задач по дому"""
        logger.info("Получение всех задач по дому через менеджер")
        try:
            result = self.db_entity.get_all_housework_tasks()
            logger.info(f"Получено {len(result)} задач по дому")
            return result
        except Exception as e:
            logger.error(f"Ошибка при получении задач по дому: {e}")
            raise
    
    def get_housework_task_by_id(self, task_id: int) -> Optional[tuple]:
        """Получение задачи по дому по ID"""
        logger.info(f"Получение задачи по дому по ID: {task_id}")
        try:
            result = self.db_entity.get_housework_task_by_id(task_id)
            if result:
                logger.info(f"Задача по дому с ID {task_id} найдена")
            else:
                logger.info(f"Задача по дому с ID {task_id} не найдена")
            return result
        except Exception as e:
            logger.error(f"Ошибка при получении задачи по дому с ID {task_id}: {e}")
            raise

    def update_housework_task(self, task_id: int, name: str = None, duration: int = None,
                             frequency: str = None, last_completed: date = None):
        """Обновление задачи по дому"""
        logger.info(f"Обновление задачи по дому с ID: {task_id}")
        try:
            self.db_entity.update_housework_task(task_id, name, duration, frequency, last_completed)
            logger.info(f"Задача по дому с ID {task_id} обновлена")
        except Exception as e:
            logger.error(f"Ошибка при обновлении задачи по дому с ID {task_id}: {e}")
            raise

    def delete_housework_task(self, task_id: int):
        """Удаление задачи по дому"""
        logger.info(f"Удаление задачи по дому с ID: {task_id}")
        try:
            self.db_entity.delete_housework_task(task_id)
            logger.info(f"Задача по дому с ID {task_id} удалена")
        except Exception as e:
            logger.error(f"Ошибка при удалении задачи по дому с ID {task_id}: {e}")
            raise

    def get_due_tasks(self) -> List[tuple]:
        """Получение задач, которые нужно выполнить сегодня"""
        logger.info("Получение задач, которые нужно выполнить сегодня")
        try:
            all_tasks = self.db_entity.get_all_housework_tasks()
            due_tasks = []

            today = date.today()

            for task in all_tasks:
                # task содержит 6 элементов: id, name, duration, frequency, last_completed, created_at
                task_id, name, duration, frequency, last_completed_str, created_at = task

                # Если задача никогда не выполнялась, считаем, что её пора выполнить
                if last_completed_str is None:
                    due_tasks.append(task)
                    continue

                if last_completed_str is not None:
                    last_completed = date.fromisoformat(last_completed_str)

                    # Проверяем, пора ли выполнять задачу в зависимости от частоты
                    if frequency == "daily":
                        if last_completed < today:
                            due_tasks.append(task)
                    elif frequency == "weekly":
                        week_ago = today - timedelta(days=7)
                        if last_completed < week_ago:
                            due_tasks.append(task)
                    elif frequency == "monthly":
                        month_ago = today - timedelta(days=30)
                        if last_completed < month_ago:
                            due_tasks.append(task)
                    elif frequency == "yearly":
                        year_ago = today - timedelta(days=365)
                        if last_completed < year_ago:
                            due_tasks.append(task)
                else:
                    # Если last_completed_str is None, добавляем задачу как требующую выполнения
                    due_tasks.append(task)

            logger.info(f"Найдено {len(due_tasks)} задач, которые нужно выполнить сегодня")
            return due_tasks
        except Exception as e:
            logger.error(f"Ошибка при получении задач на сегодня: {e}")
            raise

    def mark_task_completed(self, task_id: int):
        """Отметить задачу как выполненную"""
        logger.info(f"Отметка задачи с ID {task_id} как выполненной")
        try:
            today = date.today()
            self.db_entity.update_housework_task(task_id, last_completed=today)
            logger.info(f"Задача с ID {task_id} отмечена как выполненная")
        except Exception as e:
            logger.error(f"Ошибка при отметке задачи с ID {task_id} как выполненной: {e}")
            raise