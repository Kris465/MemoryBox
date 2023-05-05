from controller import Controller


class View:

    def __init__(self, controller: Controller):
        self.controller = controller

    def start(self):
        title = input("Title: ")
        controller = Controller(title)
        option = int(input("1. Check.\n2. Collect.\n3. Translate\n4. temp\n"))
        match option:
            case 1:
                controller.check()
            case 2:
                controller.collect()
            case 3:
                controller.translate()
            case 4:
                controller.temp()
