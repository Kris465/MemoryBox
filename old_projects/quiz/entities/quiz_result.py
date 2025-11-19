from dataclasses import dataclass
from typing import List


@dataclass
class QuizResult:
    """Сущность для хранения результатов викторины"""
    total_questions: int
    correct_answers: int
    score: float
    answered_questions: List[dict]

    @property
    def percentage(self) -> float:
        """Возвращает процент правильных ответов"""
        return (self.correct_answers / self.total_questions) * 100

    def display_result(self) -> str:
        """Возвращает форматированные результаты"""
        return (f"\n=== РЕЗУЛЬТАТЫ ВИКТОРИНЫ ===\n"
                f"Всего вопросов: {self.total_questions}\n"
                f"Правильных ответов: {self.correct_answers}\n"
                f"Процент правильных: {self.percentage:.1f}%\n"
                f"Оценка: {self.score:.2f}")
