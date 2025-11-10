from typing import Callable, List, Dict, Any
from loguru import logger


class UserMenu:
    """Класс для управления консольным меню"""

    def __init__(self):
        self.menu_items = []
        self.current_user = None

    def display_header(self):
        """Отображает заголовок приложения"""
        print("\n" + "="*50)
        print("ВИКТОРИНА ДЛЯ СТУДЕНТОВ")
        print("="*50)

    def display_menu(self):
        """Отображает главное меню"""
        self.display_header()
        print("\nГлавное меню:")
        for i, item in enumerate(self.menu_items, 1):
            print(f"{i}. {item['label']}")
        print("0. Выход")

    def add_menu_item(self, label: str, handler: Callable, **kwargs):
        """Добавляет пункт меню"""
        self.menu_items.append({
            'label': label,
            'handler': handler,
            'kwargs': kwargs
        })

    def get_user_choice(self) -> int:
        """Получает выбор пользователя"""
        try:
            choice = input(f"\nВыберите пункт меню (0-{len(self.menu_items)}): ").strip()
            return int(choice)
        except ValueError:
            return -1

    def run(self):
        """Запускает главный цикл меню"""
        logger.info("Запуск пользовательского меню")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == 0:
                print("\nСпасибо за участие! До свидания!")
                logger.info("Пользователь вышел из приложения")
                break
            elif 1 <= choice <= len(self.menu_items):
                menu_item = self.menu_items[choice - 1]
                logger.info(f"Выбран пункт меню: {menu_item['label']}")
                try:
                    menu_item['handler'](**menu_item.get('kwargs', {}))
                except Exception as e:
                    logger.error(f"Ошибка в обработчике меню: {e}")
                    print("Произошла ошибка. Попробуйте снова.")
            else:
                print("Неверный выбор. Попробуйте снова.")

    def display_welcome(self):
        """Отображает приветствие"""
        self.display_header()
        print("\nДобро пожаловать в образовательную викторину!")
        print("Здесь вы можете проверить свои знания в различных областях.")
        print("Выберите режим и начинайте обучение!")

    def display_user_info(self, username: str = None):
        """Отображает информацию о пользователе"""
        if username:
            print(f"\nТекущий пользователь: {username}")
        else:
            print("\nВы не авторизованы")

    def input_username(self) -> str:
        """Запрашивает имя пользователя"""
        print("\n" + "-"*30)
        username = input("Введите ваше имя: ").strip()
        if username:
            self.current_user = username
            logger.info(f"Пользователь авторизовался: {username}")
            print(f"Привет, {username}!")
            return username
        else:
            print("Имя не может быть пустым")
            return ""

    def display_categories(self, categories: List[str]):
        """Отображает доступные категории"""
        print("\nДоступные категории:")
        for i, category in enumerate(categories, 1):
            print(f"  {i}. {category}")

    def display_difficulty_levels(self):
        """Отображает уровни сложности"""
        print("\nУровни сложности:")
        print("1. Легкий")
        print("2. Средний")
        print("3. Сложный")

    def display_quiz_settings(self):
        """Отображает настройки викторины"""
        print("\nНастройки викторины:")
        print("  • Количество вопросов: настраивается")
        print("  • Таймер: опционально")
        print("  • Подсказки: доступны")

    def display_statistics_preview(self, stats: Dict[str, Any]):
        """Отображает превью статистики"""
        print("\nВаша статистика:")
        print(f"  • Пройдено викторин: {stats.get('quizzes_taken', 0)}")
        print(f"  • Лучший результат: {stats.get('best_score', 0):.1f}%")
        print(f"  • Средний результат: {stats.get('average_score', 0):.1f}%")
