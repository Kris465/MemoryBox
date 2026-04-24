from loguru import logger

from controller import Controller
from view import View


def main():
    logger.remove(0)
    logger.add(
        "file.log",
        level="INFO",
        retention="3 days",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )

    controller = Controller()
    view = View()

    while True:
        action = view.start_menu()
        if action == 5:
            print("До свидания!")
            break
        elif action in [1, 2, 3, 4]:
            controller.run(action)
        else:
            print("Неверный номер. Пожалуйста, введите число от 1 до 5")

        input("\nНажмите Enter, чтобы продолжить...")


if __name__ == '__main__':
    main()
