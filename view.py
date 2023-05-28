from controller import Controller


class View:

    def __init__(self, controller: Controller):
        self.controller = controller

    def start(self):
        option = 3
        while option != 0:
            option = int(input(
                "1. Create\n2. Update\n3. Translate\n0. Exit\n"
                ))
            match option:
                case 1:
                    self.controller.collect_chapters()
                case 2:
                    self.controller.update()
                case 3:
                    self.controller.translate()
