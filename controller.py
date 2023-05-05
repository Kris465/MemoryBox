from librarian import Librarian


class Controller:

    def __init__(self, title):
        self.title = title

    def check(self):
        librarian = Librarian(self.title)
        librarian.check_title()

    def collect(self):
        librarian = Librarian(self.title)
        librarian.check_title()
        librarian.collect()

    def translate(self):
        librarian = Librarian(self.title)
        librarian.translate()

    def temp(self):
        librarian = Librarian(self.title)
        print(librarian.chapters)
