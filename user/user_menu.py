class User_menu:
    
    def __init__(self):
        self.mode = None
        self.chapter = None
        self.title = None
        self.link = None
        
    def return_task(self):
        self.mode = input("Введите режим: ")
        self.chaper = int(input("Введите номер главы: "))
        self.title = input("Введите название проекта: ")
        self.link = input("Введите ссылку: ")
        return [self.mode, self.chapter, self.title, self.link]