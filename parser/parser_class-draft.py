import re
from parser.chapter_class import Chapter
from db_session import get_session
from models import Parser
from parser.connection import connection


class Parser_:

    def __init__(self, URL):
        self.__url = URL
        self.__tag = 'div'
        self.__cl = 'entry-content'
        self.__chapter = 0

    @property
    def cl(self):
        return self.__cl

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, URL):
        self.__url = URL

    @property
    def word(self):
        return self.__word

    @property
    def chapter(self):
        return self.__chapter

    @chapter.setter
    def chapter(self, chapter):
        self.__chapter = chapter

    def check_tags(self):
        print("Checking tags...")
        temp_url = re.sub(r'^https?://(?:www\.)?(.*?)/.*$',
                          r'\1',
                          self.__url)
        print(temp_url)
        session = get_session()
        result = session.query(Parser).filter(Parser.url == temp_url).all()
        if len(result) == 1:
            for webpage in result:
                self.__tag = webpage.tag
                self.__cl = webpage.cl
                self.__word = webpage.word
                print(self.tag, self.cl, self.word)
        elif len(result) == 0:
            self.__tag = input("tag: ")
            self.__cl = input("class: ")
            self.__word = input("word: ")
            new_webpage = Parser(url=temp_url,
                                 tag=self.__tag,
                                 cl=self.__cl,
                                 word=self.__word)
            session.add(new_webpage)
            session.commit()
        else:
            print("Check datebase!!!")



    def parse(self, mod, language):
        chapters = []
        match mod:
            case "stepper":
                link = self.url
                while link is not None:
                    if link[0] != "h":
                        self.url = 'https:/' + link
                    else:
                        self.url = link

                    result = connection(url=self.url,
                                        language=language,
                                        tag=self.tag,
                                        cl=self.cl)
                    chapter = Chapter(self.chapter,
                                      self.url,
                                      str([i.text for i in result]))
                    print(self.chapter)
                    chapters.append(chapter)
                    self.chapter = self.chapter + 1
                    links = connection(url=self.url,
                                       language=language,
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
                    if next_link == self.url:
                        next_link = None
                    link = next_link
                return chapters
            case "collector":
                path = re.sub(r'^https?://[^/]+', '', self.url)
                links = connection(url=self.url,
                                   language=language,
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
                    if link[0] == "h":
                        self.url = link
                    else:
                        self.url = 'https://www.shubaow.net' + link
                        # self.url = "https://m.shubaow.net/" + link
                    print(link, sorted_links.index(link))
                    result = connection(url=self.url,
                                        language=language,
                                        tag=self.tag,
                                        cl=self.cl)
                    print(result)
                    chapter = Chapter(sorted_links.index(link) + 1,
                                      link,
                                      str([i.text for i in result]))
                    chapters.append(chapter)
                return chapters
        return None
