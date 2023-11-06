import asyncio
from domain.controller import Controller
from loguru import logger

from domain.task_queue import TaskQueue


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True, diagnose=True)

    queue = TaskQueue()
    logger.info(f"Queue object is created / {queue.__class__.__name__}")

    print("Novels:")
    novels = list(map(str.strip, iter(input, '')))

    for order, title in enumerate(novels):
        controller = Controller(title)
        queue.add_task(controller)
        logger.info(f"Task {order} with {title} is created")

    asyncio.run(queue.run_tasks())


if __name__ == '__main__':
    main()
