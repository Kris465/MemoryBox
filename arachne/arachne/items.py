import scrapy


class ChapterItem(scrapy.Item):
    url = scrapy.Field()
    content = scrapy.Field()
    chapter_number = scrapy.Field()

    viewport = scrapy.Field()
    theme_color = scrapy.Field()
    description = scrapy.Field()
    domain = scrapy.Field()

    def to_legacy_format(self):
        return {
            str(self['chapter_number']): (
                f"{self['url']}\n"
                f"viewport: {self.get('viewport', '')}\n"
                f"theme-color: {self.get('theme_color', '')}\n"
                f"description: {self.get('description', '')}\n\n"
                f"{self['content']}"
            )
        }
