from controller import Controller
from presenter.user_menu.view import View


def main():
    view = View()
    controller = Controller(view)
    controller.logic()


if __name__ == '__main__':
    main()
