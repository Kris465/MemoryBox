import scrapy
import json
import re
from scrapy import Request
from urllib.parse import urljoin


class NovelSpider(scrapy.Spider):
    name = 'novel_spider'
    start_urls = ['https://inoveltranslation.com/novels/4fe34c97-15e2-4bca-8cef-eeee498a1d15']  # Убрал пробел

    custom_settings = {
        'DOWNLOAD_DELAY': 3,  # Увеличил задержку
        'CONCURRENT_REQUESTS': 1,
        'PLAYWRIGHT_MAX_PAGES_PER_CONTEXT': 1,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chapters_dict = {}
        self.processed_urls = set()  # Для отслеживания обработанных URL

    def start_requests(self):
        try:
            with open('chapter_links.json', 'r', encoding='utf-8') as f:
                chapters = json.load(f)
                if isinstance(chapters, list):  # Поддержка старого формата
                    self.logger.info("Найдены сохраненные ссылки на главы (старый формат)")
                    for chapter in chapters:
                        if chapter['url'] not in self.processed_urls:
                            self.processed_urls.add(chapter['url'])
                            yield Request(
                                chapter['url'],
                                meta={
                                    "playwright": True,
                                    "playwright_include_page": True,
                                    "playwright_context": "chapter_content_context",
                                    "playwright_page_goto_kwargs": {
                                        "wait_until": "networkidle",  # Более строгая проверка
                                        "timeout": 90000
                                    },
                                    "chapter_title": chapter.get('title', '')
                                },
                                callback=self.parse_chapter_content,
                                dont_filter=True
                            )
                    return
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        self.logger.info("Собираем ссылки на главы")
        for url in self.start_urls:
            yield Request(
                url,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_context": "chapter_links_context",
                    "playwright_page_goto_kwargs": {
                        "wait_until": "networkidle",
                        "timeout": 90000
                    }
                },
                callback=self.parse_chapter_links
            )

    async def parse_chapter_links(self, response):
        page = response.meta["playwright_page"]
        chapters = []

        try:
            # Добавляем дополнительную задержку
            await page.wait_for_timeout(5000)
            await page.wait_for_selector('section a[href*="/chapters/"]', timeout=60000)
            
            chapter_elements = await page.query_selector_all('section a[href*="/chapters/"]')

            for element in chapter_elements:
                href = await element.get_attribute('href')
                title = await element.text_content()
                if href and title and href not in self.processed_urls:
                    full_url = urljoin(response.url, href)
                    chapters.append({
                        'title': title.strip(),
                        'url': full_url
                    })
                    self.processed_urls.add(href)

            if chapters:
                with open('chapter_links.json', 'w', encoding='utf-8') as f:
                    json.dump(chapters, f, ensure_ascii=False, indent=2)
                self.logger.info(f"Сохранено {len(chapters)} ссылок на главы")

                for chapter in chapters:
                    yield Request(
                        chapter['url'],
                        meta={
                            "playwright": True,
                            "playwright_include_page": True,
                            "playwright_context": "chapter_content_context",
                            "playwright_page_goto_kwargs": {
                                "wait_until": "networkidle",
                                "timeout": 90000
                            },
                            "chapter_title": chapter['title']
                        },
                        callback=self.parse_chapter_content,
                        dont_filter=True
                    )
            else:
                self.logger.warning("Не найдено ни одной главы")

        except Exception as e:
            self.logger.error(f"Ошибка при сборе ссылок: {str(e)}")
            await page.screenshot(path='chapter_links_error.png', full_page=True)
        finally:
            await page.close()

    async def parse_chapter_content(self, response):
        page = response.meta["playwright_page"]
        chapter_title = response.meta.get("chapter_title", "")

        try:
            # Добавляем дополнительные проверки загрузки
            await page.wait_for_timeout(3000)
            await page.wait_for_selector('section[data-sentry-component="RichText"]', timeout=60000)
            
            # Проверяем, что контент действительно загрузился
            await page.wait_for_function(
                '''() => {
                    const el = document.querySelector('section[data-sentry-component="RichText"]');
                    return el && el.textContent.trim().length > 50;
                }''',
                timeout=60000
            )

            content = await page.query_selector('section[data-sentry-component="RichText"]')
            chapter_text = await content.text_content()
            chapter_text = " ".join(chapter_text.split()).strip()

            # Используем позицию в списке как номер главы, если не можем извлечь из заголовка
            chapter_number = self.extract_chapter_number(chapter_title) or str(len(self.chapters_dict) + 1)
            
            if chapter_text:
                self.chapters_dict[chapter_number] = f"{response.url}\n\n{chapter_text}"
                self.logger.info(f"Обработана глава {chapter_number}: {chapter_title[:50]}...")
                
                # Промежуточное сохранение после каждой главы
                with open('novel_content.json', 'w', encoding='utf-8') as f:
                    json.dump(self.chapters_dict, f, ensure_ascii=False, indent=2)
            else:
                self.logger.warning(f"Пустой текст в главе {chapter_number}")

        except Exception as e:
            self.logger.error(f"Ошибка при обработке главы {response.url}: {str(e)}")
            await page.screenshot(path=f'chapter_error_{response.url.split("/")[-1]}.png', full_page=True)
        finally:
            await page.close()

    def closed(self, reason):
        if self.chapters_dict:
            with open('novel_content.json', 'w', encoding='utf-8') as f:
                json.dump(self.chapters_dict, f, ensure_ascii=False, indent=2)
            self.logger.info(f"Итоговый результат: сохранено {len(self.chapters_dict)} глав")
        else:
            self.logger.warning("Не удалось сохранить результат - словарь глав пуст")

    @staticmethod
    def extract_chapter_number(title):
        # Более гибкое извлечение номера главы
        matches = re.findall(r'\d+', title)
        return matches[0] if matches else None
