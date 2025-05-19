import scrapy
import json


class StepperSpider(scrapy.Spider):
    name = 'stepper'
    start_url = 'https://inoveltranslation.com/chapters/8250907e-0f47-421d-aad7-5b72d5fe7164'
    chapter_counter = 1
    max_chapters = 100
    chapters = {}

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
            callback=self.parse_chapter
        )

    async def parse_chapter(self, response):
        page = response.meta["playwright_page"]

        try:
            await page.wait_for_selector(
                'section[data-sentry-component="RichText"]', timeout=30000)

            content = await page.query_selector(
                'section[data-sentry-component="RichText"]')
            chapter_text = await content.text_content()
            chapter_text = " ".join(chapter_text.split()).strip()

            self.chapters[str(self.chapter_counter)] = response.url + "\n\n" + chapter_text

            dropdown = await page.query_selector('button[role="combobox"]')
            if dropdown:
                await dropdown.click()
                await page.wait_for_timeout(1000)

                next_chapter_text = f"Ch. {self.chapter_counter + 1}"

                next_chapter_selector = f'div[role="option"]:has-text("{next_chapter_text}")'
                next_chapter_item = await page.query_selector(next_chapter_selector)

                if next_chapter_item and self.chapter_counter < self.max_chapters:
                    self.chapter_counter += 1
                    await next_chapter_item.click()
                    await page.wait_for_timeout(3000)

                    yield scrapy.Request(
                        page.url,
                        meta={
                            "playwright": True,
                            "playwright_page": page,
                            "playwright_context": "stepper-context",
                            "playwright_page_goto_kwargs": {
                                "wait_until": "networkidle",
                                "timeout": 60000
                            }
                        },
                        callback=self.parse_chapter,
                        dont_filter=True
                    )
                else:
                    print("Следующая глава не найдена или достигнут лимит")
                    await self.save_to_json()
            else:
                print("Не удалось найти дропдаун глав")
                await self.save_to_json()

        except Exception as e:
            await self.save_to_json()
            self.logger.error(f"Ошибка: {str(e)}")
            await page.close()

    async def save_to_json(self):
        with open('novel.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.chapters, json_file, ensure_ascii=False, indent=4)
        self.logger.info(f"Сохранено {len(self.chapters)} глав в novel.json")
