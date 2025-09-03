def hero_stregth(name, strength):
    if 1 <= strength <= 10:
        print(f"Супергерой {name} имеет силу {strength}")
    else:
        print("Сила должна быть от 1 до 10.")


name = input("Введите имя супергероя: ")
strength = int(input("Введите силу героя от 1 до 10: "))
hero_stregth()
