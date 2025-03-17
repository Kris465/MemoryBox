from loguru import logger

from domain.controller import Controller
from user.user_menu import User_menu


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    user_menu = User_menu()
    task = user_menu.return_task()

    controller = Controller(task)
    controller.run()

if __name__ == '__main__':
    main()