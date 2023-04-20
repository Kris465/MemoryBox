from controller import Controller
from view import View


def main():
    controller = Controller()
    view = View(controller)
    view.start()


if __name__ == '__main__':
    main()
