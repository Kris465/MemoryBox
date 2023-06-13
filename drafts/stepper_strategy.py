from parser.chapter_class import Chapter
from parser.connection import connection


class Stepper:

    def __init__(self, chapter, parser,
                 tag='div',
                 cl='entry-content',
                 language='en',
                 word='Next'):
        self.chapter_url = chapter.link
        self.tag = parser.tag
        self.cl = parser.cl
        self.language = language
        self.chapter = chapter.ordinal_number
        self.word = word

    def collect_chapters(self):
        chapters = []
        link = self.chapter_url
        while link is not None:
            result = connection(url=self.chapter_url,
                                language=self.language,
                                tag=self.tag,
                                cl=self.cl)
            chapter = Chapter(ordinal_number=self.chapter,
                              link=self.chapter_url,
                              language=self.language,
                              original_text=str([i.text for i in result]))
            print(chapter.link, chapter.ordinal_number, chapter.original_text)
            chapters.append(chapter)
            self.chapter = self.chapter + 1
            links = connection(url=self.chapter_url,
                               language=self.language,
                               tag=self.tag,
                               cl=self.cl,
                               urls=True)
            for link in links:
                if self.word.upper() in link.text.upper():
                    next_link = link['href']
                    print(next_link)
                    break
                else:
                    next_link = None
        return chapters
