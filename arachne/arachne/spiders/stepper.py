import scrapy
import json


class StepperSpider(scrapy.Spider):
    name = 'stepper'
    start_url = 'https://inoveltranslation.com/chapters/8250907e-0f47-421d-aad7-5b72d5fe7164 '

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chapter_counter = 1
        self.current_url = self.start_url
        self.chapters = {}
        self.max_chapters = 60

    def start_requests(self):
        yield scrapy.Request(
            self.start_url,
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "playwright_context": "stepper-context",
                "playwright_page_goto_kwargs": {
                    "wait_until": "networkidle",
                    "timeout": 60000
                }
            },
            callback=self.logic
        )

    async def logic(self, response):
        page = response.meta["playwright_page"]

        try:
            while self.chapter_counter <= self.max_chapters:
                result = await self.extract_chapter(page)

                if not result:
                    break

                chapter_text, next_page_url = result

                self.chapters[str(self.chapter_counter)] = self.current_url + "\n\n" + chapter_text
                self.logger.info(f"Глава {self.chapter_counter} сохранена")

                dropdown = await page.query_selector('button[role="combobox"]')
                if not dropdown:
                    self.logger.warning("Не найден дропдаун")
                    break

                await dropdown.click()
                await page.wait_for_timeout(1000)

                next_chapter_text = f"Ch. {self.chapter_counter + 1}"
                options = await page.query_selector_all('div[role="option"]')
                next_chapter_item = None

                for option in options:
                    text = await option.text_content()
                    if text.strip() == next_chapter_text:
                        next_chapter_item = option
                        break

                if next_chapter_item:
                    await next_chapter_item.click()
                    await page.wait_for_function("location.href !== arguments[0]", [self.current_url])
                    self.current_url = await page.url()
                    self.chapter_counter += 1
                else:
                    self.logger.info("Больше глав нет")
                    break

            await self.save_to_json()
            await page.close()

        except Exception as e:
            self.logger.error(f"Ошибка в логике: {str(e)}")
            await self.save_to_json()
            await page.close()

    async def extract_chapter(self, page):
        try:
            await page.wait_for_selector('section[data-sentry-component="RichText"]', timeout=60000)
            content = await page.query_selector('section[data-sentry-component="RichText"]')
            chapter_text = await content.text_content()
            chapter_text = " ".join(chapter_text.split()).strip()
            return chapter_text, page.url
        except Exception as e:
            self.logger.error(f"Ошибка при извлечении главы: {str(e)}")
            return None

    async def save_to_json(self):
        with open('novel.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.chapters, json_file, ensure_ascii=False, indent=4)
        self.logger.info(f"Сохранено {len(self.chapters)} глав в novel.json")
