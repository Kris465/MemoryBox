from controller import Controller


class View:

    def __init__(self, controller: Controller):
        self.controller = controller

    def start(self):
        option = 35
        while option != 0:
            option = int(input(
                "1. Change title\n/2. Currect_method\n"
                "3. Create project\n4. Create novel\n"
                "/5. Collect chapters\n6. Translate\n"
                "0. Exit\n"
                ))
            match option:
                case 1:
                    new_title = input()
                    self.controller.title = new_title
                    print(self.controller.title)
                case 2:
                    self.controller.parsing()
                case 3:
                    self.controller.create_project()
                case 4:
                    self.controller.create_novel()
                case 5:
                    self.controller.update()
                case 6:
                    self.controller.translate()
