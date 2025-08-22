import requests
from time import sleep
from random import randint
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from bs4 import BeautifulSoup
from loguru import logger

from tools.file_manager import read_from_json
from tools.other_tools import get_domain_name


class Checker:
    def __init__(self, link):
        self.link = link
        self.name = get_domain_name(self.link)
        self.result = False
        self.tool = ""
        self.session = requests.Session()

    def tool_box(self):
        '''
        Чтение конфига из selectors.json
        '''
        data = read_from_json("selectors.json")
        self.tool = data[self.name]["tool"]
        self.selector = data[self.name]['selector']
        logger.info(f"Инструмент для новелы: {self.link} выбран: {self.tool}")

    async def logic(self):
        self.tool_box()
        await self.parse()

    def get_page_with_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        response = self.session.get(self.link, headers=headers)
        response.encoding = response.apparent_encoding

        if response.status_code != 200:
            logger.error(f"Ошибка {response.status_code} при запросе {self.link}")
            return None

        return response.text


async def get_page_with_playwright(self):
    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()

            await page.goto(self.link, wait_until='domcontentloaded')

            await page.wait_for_timeout(5000)

            html = await page.content()

            await context.close()
            await browser.close()
            return html

    except PlaywrightTimeoutError:
        logger.error(f"Таймаут при загрузке страницы: {self.link}")
        return None
    except Exception as e:
        logger.error(f"Ошибка при работе Playwright: {e}")
        return None

    def parse_html(self, html):
        if not html:
            return False

        page = BeautifulSoup(html, 'html.parser')
        link = page.select_one(self.selector)

        if not link:
            logger.error(f"Не удалось найти элемент по селектору: {self.selector}")
            link = self.find_next_link_smart(page)
            return link

        if link.name != 'a' or not link.get('href'):
            logger.error(f"Элемент по селектору {self.selector} не является ссылкой или не имеет href")
            return False

        extracted_link = link['href']
        logger.info(f"Извлеченная ссылка: {extracted_link}")
        return extracted_link

    def find_next_link_smart(self, soup):
        """
        Умный поиск ссылки на следующую главу
        """
        next_keywords = [
            'next', 'next chapter', '→', '>', 'continue'
        ]
        all_links = soup.find_all('a', href=True)
        scored_links = []

        for link in all_links:
            text = link.get_text(strip=True).lower()
            href = link['href']
            score = 0
            for keyword in next_keywords:
                if keyword in text:
                    score += 3

            if 'chapter' in text or 'глава' in text:
                score += 2

            if href and not href.startswith(('javascript:', '#')):
                score += 1

            if score > 0 and 'http' in href:
                scored_links.append((score, href, text))
        scored_links.sort(key=lambda x: x[0], reverse=True)

        if scored_links:
            best_score, best_link, best_text = scored_links[0]
            logger.info(f"Найдена ссылка: '{best_text}' -> {best_link} (score: {best_score})")
            return best_link

        logger.error("Не удалось найти подходящую ссылку на следующую главу")
        return False

    def check_link_validity(self, extracted_link):
        if not extracted_link:
            return False

        sleep(randint(7, 20))

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': self.link
            }

            response = self.session.get(extracted_link, headers=headers)
            logger.info(f"Статус код проверки ссылки: {response.status_code}")

            if response.status_code == 200:
                self.link = extracted_link
                return True
            else:
                logger.error(f"Ошибка {response.status_code} при запросе {extracted_link}")
                return False
        except Exception as e:
            logger.error(e)
            return False

    async def parse(self):
        html = None

        match self.tool:
            case "requests":
                html = self.get_page_with_requests()
            case "playwright":
                html = await self.get_page_with_playwright()
            case _:
                logger.error(f"Неизвестный инструмент: {self.tool}")
                self.result = False
                return

        extracted_link = self.parse_html(html)
        self.result = self.check_link_validity(extracted_link)
