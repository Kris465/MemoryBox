class UserMenu:
    def __init__(self) -> None:
        self.tasks = []

    def collect_user_input():
        print("What do you want to do, Master?\n")
        while True:
            title = input("Titlte: \n")
            option = int(input("1.Parse\n2.Translate\n3.Save\n4.Exit\n"))
            match option:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case _:
                    return
