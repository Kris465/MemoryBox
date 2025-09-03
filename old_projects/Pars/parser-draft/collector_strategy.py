import re
from parser.chapter_class import Chapter
from parser.connection import connection


class Collector:

    def __init__(self, URL, chapter, parser,
                 tag='div',
                 cl='entry-content',
                 language='zh',
                 word='Next'):
        self.url = URL
        self.chapter_url = chapter.link
        self.tag = parser.tag
        self.cl = parser.cl
        self.language = chapter.language
        self.chapter = chapter.ordinal_number
        self.word = parser.word

    def collect_chapters(self):
        chapters = []
        path = re.sub(r'^https?://[^/]+', '', self.url)
        links = connection(url=self.url,
                           language=self.language,
                           tag=self.tag,
                           cl=self.cl,
                           urls=True)
        new_links = []
        for link in links:
            href = link.get('href')
            if href and href.startswith(path):
                new_links.append(href)

        sorted_links = sorted(set(new_links))
        for link in sorted_links:
            print(link, sorted_links.index(link))
            result = connection(url=self.url,
                                language=self.language,
                                tag=self.tag,
                                cl=self.cl)
            print(result)
            chapter = Chapter(sorted_links.index(link) + 1,
                              link,
                              str([i.text for i in result]))
            chapters.append(chapter)
        return chapters
