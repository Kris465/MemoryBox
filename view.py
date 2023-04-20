from controller import Controller

class View:

    def __init__(self, controller: Controller):
        self.controller = controller

    def start(self):
        option = 1
        print("1.new_novel\n2.read_novel\n3.update_novel\n4.exit\n")
        while option != 4:
            option = int(input())
            match (option):
                case 1:
                    self.controller.new_novel()
                case 2:
                    self.controller.read_novel()
                case 3:
                    self.controller.update_novel()
