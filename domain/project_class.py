class Project:
    def __init__(self,
                 english_name,
                 original_name="",
                 russian_name="",
                 rulate="",
                 language="en",
                 url="",
                 chapters=[],
                 current_chapter=0):
        self.original_name = original_name
        self.english_name = english_name
        self.russian_name = russian_name
        self.rulate = rulate
        self.language = language
        self.url = url
        self.current_chapter = current_chapter
        self.chapters = chapters

    def update():
        print("UPDATE METHOD!!!!")
        pass
