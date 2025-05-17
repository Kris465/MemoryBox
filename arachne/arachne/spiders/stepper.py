import scrapy
from playwright.async_api import TimeoutError as PlaywrightTimeoutError


class StepperSpider(scrapy.Spider):
    name = 'stepper'
    start_urls = ['https://inoveltranslation.com/chapters/8250907e-0f47-421d-aad7-5b72d5fe7164']
    chapter_counter = 1

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_context": "stepper-context",
                    "playwright_page_goto_kwargs": {
                        "wait_until": "domcontentloaded",
                        "timeout": 60000
                    }
                },
                callback=self.parse_chapter
            )

    async def parse_chapter(self, response):
        page = response.meta["playwright_page"]

        try:
            await page.wait_for_selector('section[data-sentry-component="RichText"]', timeout=10000)

            content = await page.query_selector('section[data-sentry-component="RichText"]')
            chapter_text = await content.text_content()
            chapter_text = " ".join(chapter_text.split()).strip()

            yield {str(self.chapter_counter): chapter_text}

            next_button = await page.query_selector('button.inline-flex >> svg[fill="currentColor"]')

            if next_button:
                self.chapter_counter += 1
                self.logger.info(f"Found next chapter button, moving to chapter {self.chapter_counter}")

                await next_button.click()
                await page.wait_for_selector('section[data-sentry-component="RichText"]', timeout=10000)

                yield scrapy.Request(
                    response.url,
                    meta={
                        "playwright": True,
                        "playwright_page": page,
                        "playwright_context": "stepper-context"
                    },
                    callback=self.parse_chapter,
                    dont_filter=True
                )
            else:
                self.logger.info("No more chapters found")
                await page.close()

        except PlaywrightTimeoutError:
            self.logger.error("Timeout while waiting for page elements")
            await page.close()
        except Exception as e:
            self.logger.error(f"Error processing page: {str(e)}")
            await page.close()
