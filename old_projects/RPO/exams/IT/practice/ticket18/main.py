import requests
from bs4 import BeautifulSoup
from typing import Optional
from loguru import logger

from Novel import Novel


class WebPageAnalyzer:
    def __init__(self, url: str, word: str):
        self.url = url
        self.word = word
        

def get_webpage_content(self) -> Optional[str]:
    try:
        response = requests.get(self.url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке странице: {e}")
        return None
    

def count_word_occurrences(self, html_content: Optional[str]) -> int:
    if html_content is None:
        return 0

    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text().lower()
    word = self.word.lower()
    return text.count(word)


def run(self):
    html_content = self.get_webpage_content()
    if html_content is None:
        print("не удалось загрузить страницу. Проверьте URL.")
        return
    
    count = self.count_word_occurrences(html_content)
    
    print(f"Слово '{self.word}' встречается на странице {count} раз(a).")


def beautifulSoup(self):
    page = self.get_webpage(self.url)
    chapters_list = page.find('ul', class_='list clearfix')
    elements = chapters_list.find_all('a')
    links = []
    for element in elements:
            href = element.get('href')
            if href:
                links.append(href)
                
    logger.info(f"Все ссылки на главы новеллы {self.title} собраны")
                
    for link in links:
            chapter_page = self.get_webpage(link)
            text = chapter_page.find('div', class_='book_con fix')
            self.chapters.update({str(self.chapter): link + text.text})
            logger.info(f"Глава {self.chapter} собрана по ссылке {link}")
            self.chapter += 1
            
    logger.info(f"Все тексты глав новеллы {self.title} собраны")
        
    novel = Novel(self.title)
    novel.write_novel_to_bd(self.chapters)


def get_webpage(self, url):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = response.apparent_encoding
        logger.info(f"Страница по адресу {url} доступна")
        return BeautifulSoup(response.text, 'html.parser')
    else:
        logger.error(f"Сервер вернул {response.status_code} статус")

