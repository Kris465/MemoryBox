from bs4 import BeautifulSoup
from loguru import logger


class Bot:
    def __init__(self, session):
        self.novels = []
        self.session = session

    def logic(self):
        list_of_links = self.get_all_chapters()
        self.update_chapters(list_of_links)

    def get_all_chapters(self):
        logger.info("Вызван метод get_all_novels у объекта бота")

        novel_url = 'https://tl.rulate.ru/book/95179'

        response = self.session.get(novel_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            chapters = soup.find_all('td', class_='t')

            chapter_links = []
            for chapter in chapters:
                link = chapter.find('a').get('href')
                if link:
                    chapter_links.append(link)

            logger.info(f"Найдено {len(chapter_links)} глав: {chapter_links}")
            return chapter_links
        else:
            logger.error(f"Ошибка получения страницы: {response.status_code}")
            return None

    def update_chapters(self, list_of_links):
        response = self.session.get("https://tl.rulate.ru" + list_of_links[1])
        print(response.text)
        # for link in list_of_links:
        #     response = self.session.get("https://tl.rulate.ru" + link)
        #     print(response.text)
