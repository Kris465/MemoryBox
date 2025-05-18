import scrapy
from playwright.async_api import TimeoutError as PlaywrightTimeoutError


class StepperSpider(scrapy.Spider):
    name = 'stepper'
    start_urls = ['https://inoveltranslation.com/chapters/8250907e-0f47-421d-aad7-5b72d5fe7164']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_context": "debug-context",
                    "playwright_page_goto_kwargs": {
                        "wait_until": "domcontentloaded",
                        "timeout": 60000
                    }
                },
                callback=self.parse_debug
            )

    async def parse_debug(self, response):
        page = response.meta["playwright_page"]

        try:
            next_button = await page.wait_for_selector(
                'button:has(svg[viewBox="0 0 15 15"]) >> nth=2',
                timeout=15000
            )

            await next_button.click()
            await page.wait_for_timeout(3000)
            self.logger.info(f"Текущий URL: {page.url}")

        except PlaywrightTimeoutError:
            self.logger.error("Не удалось найти кнопку")
            await page.screenshot(path="error.png", full_page=True)
        finally:
            await page.close()
