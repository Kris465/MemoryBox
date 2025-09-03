def friends_info():
    friends = []
    while True:
        name = input("Введите имя друга (или 'стоп' для выхода): ")
        if name.lower() == 'стоп':
            break
        favorite_food = input("Введите любимую еду: ")
        age = int(input("Введите возраст друга: "))
        friends.append((name, favorite_food, age))
        print("\nИнформация о друзьях: ")
        for friend in friends:
            if friend[2] > 10:
                print(f"{friend[0]} ({friend[2]} лет) любит {friend[1]}.")


friends_info()
