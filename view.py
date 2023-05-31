from controller import Controller


class View:

    def __init__(self, controller: Controller):
        self.controller = controller

    def start(self):
        option = 35
        while option != 0:
            option = int(input(
                "1. Change title\n2.Info\n3. Create\n4. Update\n0. Exit\n"
                ))
            match option:
                case 1:
                    new_title = input()
                    self.controller.title = new_title
                    print(self.controller.title)
                case 2:
                    self.controller.info()
                case 3:
                    self.controller.create()
                case 4:
                    self.controller.update()
