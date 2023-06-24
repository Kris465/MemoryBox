class View:

    def get_info(arg, self):
        return input(arg)

    def menu(self):
        option = int(input("1. Parse\n2. Translate\n0. Exit\n"))
        match option:
            case 1:
                return "parse"
            case 2:
                return "translate"
            case 0:
                return "exit"
