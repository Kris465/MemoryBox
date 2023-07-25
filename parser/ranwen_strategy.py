from parser.abstract_strategy import ParserStrategy


class Ranwen(ParserStrategy):

    def __init__(self, title, project_webpage, number=0):
        self.title = title
        self.project_webpage = project_webpage
        self.number = number

    def logic(self):
        links = self.collect_links()
        for link in links:
            soup = self.get_webpage(link)
            text = self.collect_chapter(soup)

    def get_webpage(self):
        return super().get_webpage()

    def collect_chapter(self, soup):
        pass
        return text

    def collect_links(self):
        data = self.get_webpage(self.project_webpage)

