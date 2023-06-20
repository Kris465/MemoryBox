class Chapter():
    def __init__(self,
                 ordinal_number,
                 link,
                 language,
                 original_text,
                 russian_text=""):
        self.__ordinal_number = ordinal_number
        self.__link = link
        self.__language = language
        self.__original_text = original_text
        self.__russian_text = russian_text

    @property
    def ordinal_number(self):
        return self.__ordinal_number

    @property
    def link(self):
        return self.__link

    @property
    def language(self):
        return self.__language

    @property
    def original_text(self):
        return self.__original_text

    @property
    def russian_text(self):
        return self.__russian_text
