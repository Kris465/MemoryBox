from loguru import logger
import sqlalchemy as sa
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Определяем базовый класс для моделей
Base = declarative_base()

# Определяем модель задачи
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Создаем базу данных SQLite
engine = create_engine('sqlite:///todo_list.db')
Base.metadata.create_all(engine)

# Создаем сессию для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Функция для добавления новой задачи
def add_task(task_text):
    new_task = Task(task=task_text)
    session.add(new_task)
    session.commit()
    logger.info(f'Задача добавлена: {task_text}')

# Функция для получения всех задач
def get_tasks():
    tasks = session.query(Task).all()
    for task in tasks:
        logger.info(f'ID: {task.id}, Задача: {task.task}, Выполнено: {task.is_completed}, Дата создания: {task.created_at}')

# Функция для обновления статуса задачи
def complete_task(task_id):
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        task.is_completed = True
        session.commit()
        logger.info(f'Задача с ID {task_id} отмечена как выполненная.')
    else:
        logger.info(f'Задача с ID {task_id} не найдена.')

# Функция для удаления задачи
def delete_task(task_id):
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
        logger.info(f'Задача с ID {task_id} удалена.')
    else:
        logger.info(f'Задача с ID {task_id} не найдена.')

# Пример использования функций
if __name__ == '__main__':
    add_task('Купить продукты')
    add_task('Сделать домашнее задание')
    add_task('Позвонить другу')
    
    logger.info("\nВсе задачи:")
    get_tasks()
    
    complete_task(1)  # Обновляем статус первой задачи
    
    logger.info("\nВсе задачи после обновления:")
    get_tasks()
    
    delete_task(3)  # Удаляем третью задачу
    
    logger.info("\nВсе задачи после удаления:")
    get_tasks()

# Закрываем сессию
session.close()
