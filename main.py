from interface import create_interface
from loguru import logger


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
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
