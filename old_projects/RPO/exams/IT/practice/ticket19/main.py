import datetime


class Task:
    def __init__(self, title, deadline, body):
        self.title = title
        self.deadline = deadline
        self.body = body

    def __str__(self):
        return f"{self.title} (до: {self.deadline.strftime('%Y-%m-%d')})\
            - {self.body}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline, body):
        self.tasks.append(Task(title, deadline, body))

    def view_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

    def new(self):
        sorted_tasks = sorted(self.tasks, key=lambda x: x.deadline)
        for index, task in enumerate(sorted_tasks):
            print(f"{index + 1}. {task}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Задача удалена.")
        else:
            print("Некорректный индекс задачи.")

    def edit_task(self, index, title, body):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = title
            self.tasks[index].body = body
            print("Задача обновлена.")
        else:
            print("Некорректный индекс задачи.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Удалить задачу")
        print("4. Редактировать задачу")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите заголовок задачи: ")
            deadline_str = input("Введите дату до (ГГГГ-ММ-ДД): ")
            body = input("Введите тело задачи (Комментарий): ")

            try:
                deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d')
                todo_list.add_task(title, deadline, body)
                print("Задача добавлена.")
            except ValueError:
                print("Некорректный формат даты. Пожалуйста, используйте\
                      формат ГГГГ-ММ-ДД.")

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            todo_list.view_tasks()
            if todo_list.__init__:
                todo_list.new()
            else:
                index_str = input("Введите номер задачи для удаления: ")
                try:
                    index = int(index_str) - 1
                    todo_list.delete_task(index)
                except ValueError:
                    print("Некорректный ввод. Пожалуйста,\
                        введите номер задачи.")

        elif choice == '4':
            todo_list.view_tasks()
            if todo_list.__init__:
                todo_list.new()
            else:
                index_str = input("Введите номер задачи для редактирования: ")
                try:
                    index = int(index_str) - 1
                    title = input("Введите новый заголовок задачи: ")
                    body = input("Введите новый текст задачи: ")
                    todo_list.edit_task(index, title, body)
                except ValueError:
                    print("Некорректный ввод. Пожалуйста,\
                        введите номер задачи.")

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из меню.")


if __name__ == "__main__":
    main()
