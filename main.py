from controller import Controller
from view import View


def main():
    view = View()
    controller = Controller(view)
    controller.start()


if __name__ == '__main__':
    main()
