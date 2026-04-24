from loguru import logger
from controller import controller


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} | {message}",
               level="INFO",
               rotation="10 MB")
    controller()


if __name__ == '__main__':
    main()
