import json
import subprocess
from loguru import logger
from time import sleep


def load_novels():
    try:
        with open("novels.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def check_novel(title, url):
    result = subprocess.run(
        ["scrapy", "crawl", "novel_checker", "-a", f"url={url}"],
        capture_output=True,
        text=True
    )
    logger.info(f"spider runs {url}")
    return "is_updated: True" in result.stdout


def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)

    novels = load_novels()
    logger.info(f"novels are loaded: {novels}")
    while True:
        for title, url in novels.items():
            if check_novel(title, url):
                print(f"🔥 Обновление в '{title}': {url}")
        # sleep(6 * 3600)
        sleep(100)


if __name__ == "__main__":
    main()
