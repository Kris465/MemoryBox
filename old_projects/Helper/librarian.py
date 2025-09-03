class Librarian():
    def __init__(self, worker):
        self.__worker = worker

    @property
    def name(self):
        return self.__worker

    @name.setter
    def name(self, worker):
        self.__worker = worker

    def get_chapter(self, titile, chapter):
        return "CHAPTER!"
