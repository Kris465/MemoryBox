import scrapy


class ChapterItem(scrapy.Item):
    url = scrapy.Field()
    chapter_number = scrapy.Field()
    content = scrapy.Field()
    domain = scrapy.Field()

    viewport = scrapy.Field()
    theme_color = scrapy.Field()
    description = scrapy.Field()

    def to_dict(self) -> dict:
        """Конвертирует в словарь для сохранения в JSON"""
        return {
            "url": self["url"],
            "chapter_number": self["chapter_number"],
            "content": self["content"],
            "domain": self["domain"],
            **({k: self[k] for k in ['viewport', 'theme_color', 'description'] if k in self})
        }
