from loguru import logger
from bot import BotUpdator


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation='3 days', backtrace=True, diagnose=True)

    bot = BotUpdator()
    bot.login()
    bot.fetch_chapters()


if __name__ == '__main__':
    main()
