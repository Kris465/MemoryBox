class Chapter:

    def __init__(self, name, link, rus, eng):
        self.__name = name
        self.__link = link
        self.__rus = rus
        self.__eng = eng

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def link(self):
        return self.__link
    
    @link.setter
    def link(self, link):
        self.__link = link
    
    @property
    def rus(self):
        return self.__rus
    
    @rus.setter
    def rus(self, rus):
        self.__rus = rus
    
    @property
    def eng(self):
        return self.__eng
    
    @eng.setter
    def eng(self, eng):
        self.__eng = eng
    
    def info(self):
        print(f'Name: {self.name}\nLink: {self.link}\nRus-chapter: {self.rus}\nEng-chapter: {self.eng}')
