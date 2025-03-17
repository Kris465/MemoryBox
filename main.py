<<<<<<< HEAD
from loguru import logger

from domain.controller import Controller
from user.user_menu import User_menu

=======
from interface import create_interface
from loguru import logger

>>>>>>> 39e56d6cb7d53a0f3ebcfc055748e5a8a700220b

def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
<<<<<<< HEAD
               rotation="3 days",
               backtrace=True, diagnose=True)

    user_menu = User_menu()
    task = user_menu.return_task()

    controller = Controller(task)
    controller.run()

if __name__ == '__main__':
    main()
=======
               rotation="5 days",
               backtrace=True, diagnose=True)

    try:
        task = create_interface()
    except Exception as e:
        logger.error(e)
        task = None

    print("Польовательские данные:", task)


if __name__ == "__main__":
    main()
>>>>>>> 39e56d6cb7d53a0f3ebcfc055748e5a8a700220b
