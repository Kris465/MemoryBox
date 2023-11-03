import asyncio
from domain.controller import Controller
from loguru import logger

from domain.task_queue import TaskQueue, run_controller


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    queue = TaskQueue()

    for _ in range(2):
        controller = Controller()
        queue.add_task(lambda: run_controller(controller))

    asyncio.run(queue.run_tasks())


if __name__ == '__main__':
    main()
