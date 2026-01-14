import sqlite3
from datetime import date
from typing import List, Optional, Tuple
from loguru import logger


class DBEntity:
    """
    Класс для работы с базой данных памятных дат
    """

    def __init__(self, db_path: str = "memorable_dates.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Инициализация базы данных и создание таблиц"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Таблица для хранения памятных дат
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memorable_dates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date DATE NOT NULL,
                description TEXT,
                category TEXT
            )
        """)
        
        # Таблица для истории напоминаний
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reminders_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_id INTEGER NOT NULL,
                is_active BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (date_id) REFERENCES memorable_dates (id)
            )
        """)

        # Таблица для домашних дел
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS housework_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                duration INTEGER,  -- продолжительность в минутах
                frequency TEXT,    -- как часто выполнять (daily, weekly, monthly, etc.)
                last_completed DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        conn.close()
    
    def add_memorable_date(self, name: str, date: date, description: str = None, category: str = None) -> int:
        """Добавление новой памятной даты"""
        logger.info(f"Добавление памятной даты: {name}, {date}")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO memorable_dates (name, date, description, category) VALUES (?, ?, ?, ?)",
            (name, date, description, category)
        )

        date_id = cursor.lastrowid
        conn.commit()
        conn.close()

        logger.info(f"Памятная дата {name} добавлена с ID {date_id}")
        return date_id
    
    def get_memorable_dates_by_month(self, month: int) -> List[Tuple]:
        """Получение всех памятных дат в заданном месяце"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Проверяем, есть ли колонка created_at в таблице
        cursor.execute("PRAGMA table_info(memorable_dates)")
        columns = [column[1] for column in cursor.fetchall()]

        if 'created_at' in columns:
            cursor.execute(
                "SELECT * FROM memorable_dates WHERE strftime('%m', date) = ?",
                (f"{month:02d}",)
            )
        else:
            # Если колонки created_at нет, добавляем её как NULL
            cursor.execute(
                "SELECT id, name, date, description, category, NULL as created_at FROM memorable_dates WHERE strftime('%m', date) = ?",
                (f"{month:02d}",)
            )

        results = cursor.fetchall()
        conn.close()

        return results
    
    def get_memorable_date_by_id(self, date_id: int) -> Optional[Tuple]:
        """Получение памятной даты по ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Проверяем, есть ли колонка created_at в таблице
        cursor.execute("PRAGMA table_info(memorable_dates)")
        columns = [column[1] for column in cursor.fetchall()]

        if 'created_at' in columns:
            cursor.execute(
                "SELECT * FROM memorable_dates WHERE id = ?",
                (date_id,)
            )
        else:
            # Если колонки created_at нет, добавляем её как NULL
            cursor.execute(
                "SELECT id, name, date, description, category, NULL as created_at FROM memorable_dates WHERE id = ?",
                (date_id,)
            )

        result = cursor.fetchone()
        conn.close()

        return result
    
    def get_all_memorable_dates(self) -> List[Tuple]:
        """Получение всех памятных дат"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Проверяем, есть ли колонка created_at в таблице
        cursor.execute("PRAGMA table_info(memorable_dates)")
        columns = [column[1] for column in cursor.fetchall()]

        if 'created_at' in columns:
            cursor.execute("SELECT * FROM memorable_dates")
        else:
            # Если колонки created_at нет, добавляем её как NULL
            cursor.execute("SELECT id, name, date, description, category, NULL as created_at FROM memorable_dates")

        results = cursor.fetchall()
        conn.close()

        return results
    
    def update_memorable_date(self, date_id: int, name: str = None, date: date = None, 
                             description: str = None, category: str = None):
        """Обновление памятной даты"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        fields = []
        values = []
        
        if name is not None:
            fields.append("name = ?")
            values.append(name)
        if date is not None:
            fields.append("date = ?")
            values.append(date)
        if description is not None:
            fields.append("description = ?")
            values.append(description)
        if category is not None:
            fields.append("category = ?")
            values.append(category)
        
        if fields:
            query = f"UPDATE memorable_dates SET {', '.join(fields)} WHERE id = ?"
            values.append(date_id)
            
            cursor.execute(query, values)
            conn.commit()
        
        conn.close()
    
    def delete_memorable_date(self, date_id: int):
        """Удаление памятной даты"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM memorable_dates WHERE id = ?", (date_id,))
        conn.commit()
        conn.close()
    
    def add_reminder_record(self, date_id: int, is_active: bool = True):
        """Добавление записи в историю напоминаний"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO reminders_history (date_id, is_active) VALUES (?, ?)",
            (date_id, is_active)
        )
        
        conn.commit()
        conn.close()
    
    def get_reminder_records(self, date_id: int = None) -> List[Tuple]:
        """Получение записей из истории напоминаний"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if date_id is not None:
            cursor.execute(
                "SELECT * FROM reminders_history WHERE date_id = ? ORDER BY created_at DESC",
                (date_id,)
            )
        else:
            cursor.execute("SELECT * FROM reminders_history ORDER BY created_at DESC")

        results = cursor.fetchall()
        conn.close()

        return results

    def add_housework_task(self, name: str, duration: int = None, frequency: str = None, last_completed: date = None) -> int:
        """Добавление новой задачи по дому"""
        logger.info(f"Добавление задачи по дому: {name}")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO housework_tasks (name, duration, frequency, last_completed) VALUES (?, ?, ?, ?)",
            (name, duration, frequency, last_completed)
        )

        task_id = cursor.lastrowid
        conn.commit()
        conn.close()

        logger.info(f"Задача по дому {name} добавлена с ID {task_id}")
        return task_id

    def get_all_housework_tasks(self) -> List[Tuple]:
        """Получение всех задач по дому"""
        logger.info("Получение всех задач по дому")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM housework_tasks")

        results = cursor.fetchall()
        conn.close()

        logger.info(f"Получено {len(results)} задач по дому")
        return results

    def get_housework_task_by_id(self, task_id: int) -> Optional[Tuple]:
        """Получение задачи по дому по ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM housework_tasks WHERE id = ?",
            (task_id,)
        )

        result = cursor.fetchone()
        conn.close()

        return result

    def update_housework_task(self, task_id: int, name: str = None, duration: int = None,
                            frequency: str = None, last_completed: date = None):
        """Обновление задачи по дому"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        fields = []
        values = []

        if name is not None:
            fields.append("name = ?")
            values.append(name)
        if duration is not None:
            fields.append("duration = ?")
            values.append(duration)
        if frequency is not None:
            fields.append("frequency = ?")
            values.append(frequency)
        if last_completed is not None:
            fields.append("last_completed = ?")
            values.append(last_completed)

        if fields:
            query = f"UPDATE housework_tasks SET {', '.join(fields)} WHERE id = ?"
            values.append(task_id)

            cursor.execute(query, values)
            conn.commit()

        conn.close()

    def delete_housework_task(self, task_id: int):
        """Удаление задачи по дому"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM housework_tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()