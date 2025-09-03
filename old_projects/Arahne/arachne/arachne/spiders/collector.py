import scrapy
import json
import re
from scrapy import Request


class Collector(scrapy.Spider):
    name = 'collector'
    start_urls = ['https://volarereads.com/story/after-the-marriage-agreement-with-the-powerful-man/']

    custom_settings = {
        'DOWNLOAD_DELAY': 5,
        'CONCURRENT_REQUESTS': 1,
        'PLAYWRIGHT_MAX_PAGES_PER_CONTEXT': 1,
        'PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT': 120000,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chapters_dict = {}
        self.processed_urls = set()

    async def start(self):
        try:
            with open('chapter_links.json', 'r', encoding='utf-8') as f:
                chapters = json.load(f)
                if isinstance(chapters, list):
                    self.logger.info("Found saved chapter links (old format)")
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
                                        "wait_until": "domcontentloaded",
                                        "timeout": 120000
                                    },
                                    "chapter_title": chapter.get('title', '')
                                },
                                callback=self.parse_chapter_content,
                                dont_filter=True
                            )
                    return
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        self.logger.info("Collecting chapter links")
        for url in self.start_urls:
            yield Request(
                url,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_context": "chapter_links_context",
                    "playwright_page_goto_kwargs": {
                        "wait_until": "domcontentloaded",
                        "timeout": 120000
                    }
                },
                callback=self.parse_chapter_links
            )

    async def parse_chapter_links(self, response):
        page = response.meta["playwright_page"]
        chapters = []

        try:
            await page.wait_for_selector('.chapter-group__list', state='visible', timeout=60000)
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            await page.wait_for_timeout(3000)

            show_more_button = await page.query_selector('.chapter-group__folding-toggle')
            if show_more_button:
                await show_more_button.click()
                await page.wait_for_timeout(5000)

            chapter_elements = await page.query_selector_all('.chapter-group__list-item._publish a.chapter-group__list-item-link')

            for element in chapter_elements:
                href = await element.get_attribute('href')
                title = await element.text_content()
                if href and title and href not in self.processed_urls:
                    chapters.append({
                        'title': title.strip(),
                        'url': href
                    })
                    self.processed_urls.add(href)

            if chapters:
                with open('chapter_links.json', 'w', encoding='utf-8') as f:
                    json.dump(chapters, f, ensure_ascii=False, indent=2)
                self.logger.info(f"Saved {len(chapters)} chapter links")

                for chapter in chapters:
                    yield Request(
                        chapter['url'],
                        meta={
                            "playwright": True,
                            "playwright_include_page": True,
                            "playwright_context": "chapter_content_context",
                            "playwright_page_goto_kwargs": {
                                "wait_until": "domcontentloaded",
                                "timeout": 120000
                            },
                            "chapter_title": chapter['title']
                        },
                        callback=self.parse_chapter_content,
                        dont_filter=True
                    )
            else:
                self.logger.warning("No chapters found")

        except Exception as e:
            self.logger.error(f"Error collecting links: {str(e)}")
            await page.screenshot(path='chapter_links_error.png', full_page=True)
            raise
        finally:
            await page.close()

    async def parse_chapter_content(self, response):
        page = response.meta["playwright_page"]
        chapter_title = response.meta.get("chapter_title", "")

        try:
            await page.wait_for_selector('#chapter-content', state='visible', timeout=60000)

            await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            await page.wait_for_timeout(2000)

            content = await page.query_selector('#chapter-content')
            chapter_text = await content.text_content()
            chapter_text = " ".join(chapter_text.split()).strip()

            chapter_number = self.extract_chapter_number(chapter_title) or str(len(self.chapters_dict) + 1)
            
            if chapter_text:
                self.chapters_dict[chapter_number] = f"{response.url}\n\n{chapter_text}"
                self.logger.info(f"Processed chapter {chapter_number}: {chapter_title[:50]}...")
                
                with open('novel_content.json', 'w', encoding='utf-8') as f:
                    json.dump(self.chapters_dict, f, ensure_ascii=False, indent=2)
            else:
                self.logger.warning(f"Empty content in chapter {chapter_number}")

        except Exception as e:
            self.logger.error(f"Error processing chapter {response.url}: {str(e)}")
            await page.screenshot(path=f'chapter_error_{response.url.split("/")[-1]}.png', full_page=True)
            raise
        finally:
            await page.close()

    def closed(self, reason):
        if self.chapters_dict:
            with open('novel_content.json', 'w', encoding='utf-8') as f:
                json.dump(self.chapters_dict, f, ensure_ascii=False, indent=2)
            self.logger.info(f"Final result: saved {len(self.chapters_dict)} chapters")
        else:
            self.logger.warning("Failed to save result - chapters dictionary is empty")

    @staticmethod
    def extract_chapter_number(title):
        matches = re.findall(r'\b(\d+)\b', title)
        return matches[-1] if matches else None