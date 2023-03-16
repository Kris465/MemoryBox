from controller import Controller
from viewconsole import ViewConsole


def main():
    controller = Controller()
    vc = ViewConsole(controller)
    vc.start()


if __name__ == '__main__':
    main()
