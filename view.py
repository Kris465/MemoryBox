from controller import Controller

class View:

    def __init__(self, controller: Controller):
        self.controller = controller

    def start(self):
        title = input("Title: ")
        controller = Controller()
        controller.librarian(title)
