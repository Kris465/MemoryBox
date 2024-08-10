import requests
import json
from loguru import logger


class WebParser:
    def __init__(self, url):
        self.url = url
        self.response = None

    def fetch(self):
        """Получает ответ от сервера."""
        try:
            logger.info(f"Отправка запроса на {self.url}")
            self.response = requests.get(self.url)
            self.response.raise_for_status()  # Проверка на ошибки HTTP
            logger.info("Запрос выполнен успешно")
        except requests.RequestException as e:
            logger.error(f"Ошибка при запросе: {e}")
            self.response = None

    def get_status_code(self):
        """Возвращает статус-код ответа."""
        if self.response:
            return self.response.status_code
        else:
            logger.warning("Ответ не получен. Статус-код недоступен.")
            return None

    def save_html(self):
        """Сохраняет HTML-код страницы в файл."""
        if self.response:
            with open("page.html", 'w', encoding='utf-8') as file:
                file.write(self.response.text)
            logger.info(f"HTML-код сохранен в {self.url}")
        else:
            logger.warning("Ответ не получен. HTML-код не сохранен.")

    def save_cookies(self):
        """Сохраняет куки в файл."""
        if self.response:
            with open("cookies.txt", 'w', encoding='utf-8') as file:
                json.dump(self.response.cookies.get_dict(), file)
            logger.info(f"Куки сохранены в {self.url}_cookies")
        else:
            logger.warning("Ответ не получен. Куки не сохранены.")

    def get_headers(self):
        """Возвращает заголовки ответа."""
        if self.response:
            return dict(self.response.headers)
        else:
            logger.warning("Ответ не получен. Заголовки недоступны.")
            return None
