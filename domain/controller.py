class Controller:
    
    def logic(self):
        title = input("Title: ")
        chapter = int(input("Chapter: "))
        url = input("url: ")
        pars = Parser(title, chapter, url)
