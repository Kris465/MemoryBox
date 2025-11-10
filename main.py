import sys
import os

from typing import List, Optional, Dict, Any

from loguru import logger

from entities.question import Question
from entities.quiz_result import QuizResult
from utils.file_reader import FileReader
from ui.user_menu import UserMenu


class QuizApplication:
    """Основной класс приложения Викторина"""

    def __init__(self):
        self.questions: List[Question] = []
        self.user_stats: Dict[str, Any] = {}
        self.menu = UserMenu()
        self.setup_logging()
        self.setup_menu()

    def setup_logging(self):
        """Настройка логирования"""
        # Создаем папку для логов если её нет
        os.makedirs('logs', exist_ok=True)

        logger.remove()
        logger.add(
            sys.stderr,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            level="INFO",
            colorize=True
        )
        logger.add(
            "logs/quiz.log",
            rotation="10 MB",
            retention="1 month",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
            level="DEBUG"
        )

    def setup_menu(self):
        """Настройка пунктов меню"""
        self.menu.add_menu_item("Начать викторину", self.start_quiz_flow)
        self.menu.add_menu_item("Настройки викторины", self.show_quiz_settings)
        self.menu.add_menu_item("Статистика", self.show_statistics)
        self.menu.add_menu_item("Сменить пользователя", self.change_user)
        self.menu.add_menu_item("О программе", self.show_about)

    def load_questions(self, file_path: str = "questions.json") -> bool:
        """Загружает вопросы из файла"""
        logger.info(f"Загрузка вопросов из файла: {file_path}")
        self.questions = FileReader.read_questions_from_json(file_path)

        if not self.questions:
            logger.error("Не удалось загрузить вопросы")
            return False

        return True

    def start_quiz_flow(self):
        """Полный процесс запуска викторины"""
        if not self.menu.current_user:
            self.change_user()
            if not self.menu.current_user:
                return

        if not self.questions:
            if not self.load_questions():
                print("Ошибка загрузки вопросов")
                return

        self.configure_quiz()
        result = self.run_quiz()

        if result:
            self.display_results(result)
            self.update_statistics(result)

    def configure_quiz(self):
        """Настройка параметров викторины"""
        print("\n⚙️  Настройка викторины")
        print("-" * 30)

        # Выбор категории
        categories = list(set(q.category for q in self.questions))
        self.menu.display_categories(categories)

        # Выбор сложности
        self.menu.display_difficulty_levels()

        # Выбор количества вопросов
        max_questions = len(self.questions)
        print(f"\nДоступно вопросов: {max_questions}")

        input("\nНажмите Enter чтобы начать стандартную викторину...")

    def run_quiz(self) -> Optional[QuizResult]:
        """Запускает викторину"""
        logger.info(f"Начало викторины для пользователя: {self.menu.current_user}")

        print("\n" + "="*50)
        print(f"   ВИКТОРИНА ДЛЯ: {self.menu.current_user}")
        print("="*50)

        correct_count = 0
        answered_questions = []

        for i, question in enumerate(self.questions, 1):
            print(f"\nВопрос {i} из {len(self.questions)}")
            print(f"Категория: {question.category} | Сложность: {question.difficulty}")

            answer = self.get_user_answer(question)
            if answer is None:
                logger.info("Пользователь завершил викторину досрочно")
                print("\nВикторина прервана пользователем")
                break

            is_correct = question.is_correct(answer)
            if is_correct:
                correct_count += 1
                print("Правильно!")
            else:
                print(f"Неправильно! Правильный ответ: {question.options[question.correct_answer-1]}")

            answered_questions.append({
                'question_id': question.id,
                'user_answer': answer,
                'correct': is_correct
            })

        return self.calculate_results(correct_count,
                                      len(self.questions),
                                      answered_questions)

    def get_user_answer(self, question: Question) -> Optional[int]:
        """Получает ответ пользователя"""
        try:
            print(question.display_question())
            answer = input("Введите номер правильного ответа (1-4) или 'q' для выхода: ").strip()

            if answer.lower() == 'q':
                return None

            if not answer:
                return None

            answer_num = int(answer)
            if 1 <= answer_num <= len(question.options):
                return answer_num
            else:
                print("Пожалуйста, введите число от 1 до 4")
                return self.get_user_answer(question)  # Рекурсивный вызов для повторного ввода

        except ValueError:
            print("Пожалуйста, введите число")
            return self.get_user_answer(question)  # Рекурсивный вызов для повторного ввода
        except KeyboardInterrupt:
            logger.info("Пользователь прервал ввод")
            return None

    def calculate_results(self, correct_count: int, total_questions: int,
                          answered_questions: List[dict]) -> QuizResult:
        """Рассчитывает результаты викторины"""
        score = (correct_count / total_questions) * 10 if total_questions > 0 else 0

        result = QuizResult(
            total_questions=total_questions,
            correct_answers=correct_count,
            score=score,
            answered_questions=answered_questions
        )

        logger.info(f"Викторина завершена. Результат: {correct_count}/{total_questions}")
        return result

    def display_results(self, result: QuizResult):
        """Отображает результаты викторины"""
        print("\n" + "="*50)
        print("           РЕЗУЛЬТАТЫ ВИКТОРИНЫ")
        print("="*50)

        print(result.display_result())

        # Визуальная оценка
        if result.percentage >= 90:
            print("Потрясающе! Вы настоящий эксперт!")
        elif result.percentage >= 75:
            print("Отличный результат!")
        elif result.percentage >= 60:
            print("Хорошая работа!")
        elif result.percentage >= 50:
            print("Неплохо, но есть куда стремиться!")
        else:
            print("Продолжайте учиться! Вы сможете лучше!")

        input("\nНажмите Enter чтобы вернуться в меню...")

    def update_statistics(self, result: QuizResult):
        """Обновляет статистику пользователя"""
        user = self.menu.current_user or "Anonymous"

        if user not in self.user_stats:
            self.user_stats[user] = {
                'quizzes_taken': 0,
                'total_score': 0,
                'best_score': 0
            }

        stats = self.user_stats[user]
        stats['quizzes_taken'] += 1
        stats['total_score'] += result.percentage

        if result.percentage > stats['best_score']:
            stats['best_score'] = result.percentage

        stats['average_score'] = stats['total_score'] / stats['quizzes_taken']

        logger.info(f"Статистика обновлена для {user}")

    def show_quiz_settings(self):
        """Показывает настройки викторины"""
        self.menu.display_quiz_settings()
        input("\nНажмите Enter чтобы вернуться...")

    def show_statistics(self):
        """Показывает статистику пользователя"""
        if not self.menu.current_user:
            print("Сначала войдите в систему")
            self.change_user()
            if not self.menu.current_user:
                return

        user = self.menu.current_user
        stats = self.user_stats.get(user, {})

        if not stats:
            print("\nУ вас пока нет статистики. Пройдите первую викторину!")
        else:
            self.menu.display_statistics_preview(stats)

        input("\nНажмите Enter чтобы вернуться...")

    def change_user(self):
        """Смена пользователя"""
        username = self.menu.input_username()
        if username:
            print(f"Добро пожаловать, {username}!")
        return username

    def show_about(self):
        """Показывает информацию о программе"""
        print("\n" + "="*50)
        print("             О ПРОГРАММЕ")
        print("="*50)
        print("Виртуальная Викторина v1.0")
        print("Образовательное приложение для студентов")
        print("\nВозможности:")
        print("  • Различные категории вопросов")
        print("  • Адаптивная сложность")
        print("  • Подробная статистика")
        print("  • Система достижений")
        print("\nРазработано для учебных целей")
        print("Архитектура: MVC с отдельным UI слоем")
        input("\nНажмите Enter чтобы вернуться...")

    def run(self):
        """Запускает приложение"""
        logger.info("Запуск приложения Викторина")

        # Загрузка вопросов
        if not self.load_questions():
            print("Вопросы не загружены. Проверьте файл questions.json")

        # Приветствие
        self.menu.display_welcome()

        # Запуск меню
        self.menu.run()


def main():
    """Точка входа в приложение"""
    try:
        app = QuizApplication()
        app.run()
    except KeyboardInterrupt:
        print("\n\nПриложение завершено пользователем")
        logger.info("Приложение завершено по Ctrl+C")
    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}")
        print("Произошла критическая ошибка. Проверьте логи.")


if __name__ == "__main__":
    main()
    