import scrapy


class TestSpider(scrapy.Spider):
    name = "awesome"

    async def start_requests(self):
        yield scrapy.Request(
            url="https://www.lanry.space/novels/my-wife-conquers-the-realm/c1",
            meta={"playwright": True, "playwright_include_page": True},
            callback=self.parse,
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.screenshot(path="debug.png")
        await page.close()
        return {"url": response.url}
