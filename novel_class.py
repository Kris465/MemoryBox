class Novel():
    def __init__(self,
                 russian_name,
                 english_name,
                 webpage,
                 original_name="",
                 notes=""):
        self.__russian_name = russian_name
        self.__original_name = original_name
        self.__english_name = english_name
        self.__notes = notes
        self.__webpage = webpage
