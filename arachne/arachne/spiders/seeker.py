# from scrapy_playwright.page import PageMethod


# yield scrapy.Request(
#     url,
#     meta={
#         "playwright": True,
#         "playwright_page_methods": [
#             PageMethod("wait_for_selector", config["content_selector"]),
#         ],
#     },
#     callback=self.parse_chapter
# )