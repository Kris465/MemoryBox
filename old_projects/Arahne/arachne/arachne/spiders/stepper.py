import scrapy
import json
from scrapy import Request


class Stepper(scrapy.Spider):
    name = 'stepper'
    start_urls = ['https://inoveltranslation.com/novels/4fe34c97-15e2-4bca-8cef-eeee498a1d15']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(
                url,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_context": "chapter_links_context",
                    "playwright_page_goto_kwargs": {
                        "wait_until": "domcontentloaded",
                        "timeout": 60000
                    }
                },
                callback=self.parse_chapter_links
            )

    async def parse_chapter_links(self, response):
        page = response.meta["playwright_page"]
        chapters = []

        try:
            await page.wait_for_selector(
                'section a[href*="/chapters/"]',
                timeout=30000
            )

            chapter_elements = await page.query_selector_all(
                'section a[href*="/chapters/"]')

            for element in chapter_elements:
                href = await element.get_attribute('href')
                title = await element.text_content()

                if href and title:
                    chapters.append({
                        'title': title.strip(),
                        'url': response.urljoin(href)
                    })

            if chapters:
                with open('chapter_links.json', 'w', encoding='utf-8') as f:
                    json.dump(chapters, f, ensure_ascii=False, indent=2)
                self.logger.info(f"Successfully saved {len(chapters)} chapters")
            else:
                self.logger.warning("No chapters found")

        except Exception as e:
            self.logger.error(f"Error extracting chapters: {str(e)}")
            await page.screenshot(path='chapter_links_error.png',
                                  full_page=True)
        finally:
            await page.close()
