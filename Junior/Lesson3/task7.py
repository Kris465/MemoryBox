def todo_list():
    tasks = []
    
    while True:
        action = input("Введите 'add' для добавления задачи, 'remove' для удаления, 'show' для показа задач или 'exit' для выхода: ")
        
        if action.lower() == 'add':
            task = input("Введите задачу: ")
            tasks.append(task)
            print(f"Задача '{task}' добавлена.")
        elif action.lower() == 'remove':
            task = input("Введите задачу для удаления: ")
            if task in tasks:
                tasks.remove(task)
                print(f"Задача '{task}' удалена.")
            else:
                print("Задача не найдена.")
        elif action.lower() == 'show':
            print("Список дел:")
            for task in tasks:
                print(f"- {task}")
        elif action.lower() == 'exit':
            break
        else:
            print("Неизвестная команда.")

todo_list()
