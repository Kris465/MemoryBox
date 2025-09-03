import json

from loguru import logger


class Novel:
    def __init__(self, title):
        self.title = title
        self.chapters = {}
        
    def write_novel_to_bd(self, chapters):
        self.chapters = chapters
        with open(f"{self.title}.json", 'w', encoding='UTF-8') as json_file:
            json.dump(self.chapters, json_file, ensure_ascii=False)
        logger.info(f"Главы новеллы записаны в файл {self.title}.json")

    def load_novel_from_bd(self):
        try:
            with open(f"{self.title}.json", 'r', encoding='UTF-8') as json_file:
                self.chapters = json.load(json_file)
        except FileNotFoundError:
            logger.error(f"Файл {self.title}.json не найден")
        except json.JSONDecodeError:
            logger.error(f"Ошибка декодирования JSON")
            
    def print_novel_to_terminal(self):
        logger.info("Приступаю к распечатыванию новеллы...")
        print(f"Название {self.title}")
        print(f"Главы: ")
        for chapter_title, chapter_content in self.chapters.items():
            print(f"{chapter_title}: {chapter_content}")