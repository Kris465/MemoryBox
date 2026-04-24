import json
from pathlib import Path
from typing import List
from loguru import logger
from entities.question import Question


class FileReader:
    """Утилита для чтения вопросов из файла"""

    @staticmethod
    def read_questions_from_json(file_path: str) -> List[Question]:
        """
        Читает вопросы из JSON файла и преобразует их в список объектов Question
        
        Args:
            file_path: Путь к JSON файлу с вопросами
            
        Returns:
            List[Question]: Список объектов Question
        """
        try:
            path = Path(file_path)
            
            if not path.exists():
                logger.error(f"Файл {file_path} не найден")
                return []

            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            questions = []
            for item in data.get('questions', []):
                try:
                    question = Question(
                        id=item['id'],
                        text=item['text'],
                        options=item['options'],
                        correct_answer=item['correct_answer'],
                        category=item.get('category', 'Общие'),
                        difficulty=item.get('difficulty', 'Средняя')
                    )
                    questions.append(question)
                except KeyError as e:
                    logger.warning(f"Пропущен вопрос с ошибкой в данных: {e}")
                    continue

            logger.info(f"Успешно загружено {len(questions)} вопросов")
            return questions

        except json.JSONDecodeError as e:
            logger.error(f"Ошибка парсинга JSON: {e}")
            return []
        except Exception as e:
            logger.error(f"Неожиданная ошибка при чтении файла: {e}")
            return []
