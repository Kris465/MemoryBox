import asyncio
from loguru import logger

from domain.controller import Controller
from user.user_menu import UserMenu


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    user_menu = UserMenu()
    tasks = user_menu.menu()
    logger.info(f"Pack of tasks is created: \n"
                f"{[print(task.title) for task in tasks]}")

    controller = Controller(tasks)
    await controller.run()


if __name__ == '__main__':
    asyncio.run(main())
