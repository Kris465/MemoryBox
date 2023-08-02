# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

friends = {}


def missing_items():
    missing_dict = {}
    for item in set.union(*[set(items) for items in friends.values()]):
        missing_dict[item] = []
        for friend, items in friends.items():
            if item not in items:
                missing_dict[item].append(friend)
    for item, friends in missing_dict.items():
        if len(friends) == len(friends.keys()) - 1:
            print(item, "есть у всех друзей кроме", friends[0])


def add_friend():
    name = input("Введите имя друга: ")
    items = tuple(input(
        "Введите вещи, которые он взял через запятую: ").split(","))
    friends[name] = items
    print("Друг", name, "добавлен в список.")


def add_items():
    name = input("Введите имя друга: ")
    if name in friends:
        items = tuple(input(
            "Введите вещи, которые он добавил через запятую: ").split(","))
        new_items = friends[name] + items
        friends[name] = new_items
        print("Вещи добавлены.")
    else:
        print("Такого друга нет в списке.")


def show_friends():
    print("Список друзей и их вещей:")
    for friend in friends:
        print(friend, ":", friends[friend])


def common_items():
    common = set.intersection(*[set(items) for items in friends.values()])
    if len(common) > 0:
        print("Все друзья взяли следующие вещи:", ", ".join(common))
    else:
        print("Нет общих вещей у всех друзей.")


def unique_items():
    unique = set()
    for items in friends.values():
        unique.update(set(items))
    for item in unique:
        count = sum([1 for items in friends.values() if item in items])
        if count == 1:
            print(item, "есть только у одного друга.")


while True:
    print("\nМеню:")
    print("1. Добавить друга")
    print("2. Добавить вещи другу")
    print("3. Показать список друзей и их вещей")
    print("4. Показать общие вещи у всех друзей")
    print("5. Показать уникальные вещи")
    print("6. Показать вещи, которые есть у всех кроме одного друга")
    print("0. Выход")
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        add_friend()
    elif choice == "2":
        add_items()
    elif choice == "3":
        show_friends()
    elif choice == "4":
        common_items()
    elif choice == "5":
        unique_items()
    elif choice == "6":
        missing_items()
    elif choice == "0":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
