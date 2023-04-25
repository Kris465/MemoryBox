class Translator:

    def __init__(self, name, eng):
        self.__name = name
        self.__eng = eng
        self.__rus = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def eng(self):
        return self.__eng

    @eng.setter
    def eng(self, eng):
        self.__eng = eng

    @property
    def rus(self):
        return self.__rus
    
    @rus.setter
    def rus(self, rus):
        self.__rus = rus

    def info(self):
        print("I'm a translator")
