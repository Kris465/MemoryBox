from loguru import logger

from controller import controller


def main():
    logger.add('file.log',
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days")

    logger.info("Программа запущена!")
    controller()

 
if __name__ == '__main__':
    main()
