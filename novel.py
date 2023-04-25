# URL = read(title) хочу использовать для проверки обновлений. Надо по названию брать ссылку на проект из списка и проверять, есть ли новые главы.

class Novel:

    def __init__(self, title, chapters):
        self.__title = title
        self.__chapters = chapters

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def chapters(self):
        return self.__chapters

    @chapters.setter
    def chapters(self, chapters):
        self.__chapters = chapters

    def info(self):
        print("I'm a Novel!")
