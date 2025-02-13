from loguru import logger

from novel import Novel
from parser import Parser

def main():
    logger.add("file.log",
            format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
            rotation="3 days",
            backtrace=True, diagnose=True)
    
    title = input("Введите название новеллы: ")
    url = input("Введите ссылку с оглавнением: ")
    try:
        pars = Parser(title, url)
        pars.get_novel()
    except Exception as e:
        logger.error(f"program failed with {e}")
    
    novel = Novel(title)
    novel.load_novel_from_db()
    novel.print_novel_to_terminal()

if __name__ == '__main__':
    main()
