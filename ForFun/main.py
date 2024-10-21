from reader import Reader
from task_generator import TaskGenerator
from user_menu import UserMenu


def main():
    reader = Reader()
    all_tasks = reader.collect_all_tasks()
    tasks_generator = TaskGenerator(30, all_tasks)
    chosen_tasks = tasks_generator.choose_tasks()
    user_menu = UserMenu(chosen_tasks)
    user_menu.run()


if __name__ == '__main__':
    main()
