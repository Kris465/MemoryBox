from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Question:
    """Сущность вопроса викторины"""
    id: int
    text: str
    options: List[str]
    correct_answer: int
    category: Optional[str] = None
    difficulty: Optional[str] = None

    def is_correct(self, answer: int) -> bool:
        """Проверяет правильность ответа"""
        return answer == self.correct_answer

    def display_question(self) -> str:
        """Возвращает форматированный текст вопроса"""
        question_text = f"\n{self.text}\n"
        for i, option in enumerate(self.options, 1):
            question_text += f"{i}. {option}\n"
        return question_text
