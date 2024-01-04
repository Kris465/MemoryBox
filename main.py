from loguru import logger

from domain.controller import Controller
from storage.redis_srotage import RedisStorage
from user.user_menu import UserMenu


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    redis_storage = RedisStorage()
    logger.info("Redis is created")
    user_menu = UserMenu(redis_storage)
    logger.info("User menu is created")
    tasks = await user_menu.menu()

    controller = Controller(tasks)
    await controller.run()
