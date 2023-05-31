from controller import Controller
from repository_class import Repository
from view import View


def main():
    repository = Repository()
    controller = Controller(repository)
    view = View(controller)
    view.start()


if __name__ == '__main__':
    main()
