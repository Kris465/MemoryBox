from domain.controller import Controller
from loguru import logger
from user.user_menu import UserMenu


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    user_menu = UserMenu()
    tasks = user_menu.collect_user_input()
    logger.info(f"Pack of tasks is created: \n"
                f"{[print(task) for task in tasks]}")

    controller = Controller(tasks)
    controller.run()


if __name__ == 'main':
    main()
