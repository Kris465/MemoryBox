from loguru import logger


class View:
    def __init__(self):
        self.action = ""

    def start_menu(self):
        logger.info("Пользовательское меню вызвано")
        print("\n=== Я - приложение Заметки ===")
        print("1. Создать заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Посмотреть все заметки")
        print("5. Выйти")

        try:
            action = int(input("\nВведите номер действия: "))
            return action
        except ValueError:
            print("Пожалуйста, введите число от 1 до 5")
            return self.start_menu()
