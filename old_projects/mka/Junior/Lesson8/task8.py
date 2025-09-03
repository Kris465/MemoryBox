def hero_victories(name, victories):
    print(f"Супергерой {name} имеет {victories} побед.")


super_hero = input("Введите имя супрегероя: ")
victories = int(input("Введите количество побед супергероя: "))
hero_victories(super_hero, victories)