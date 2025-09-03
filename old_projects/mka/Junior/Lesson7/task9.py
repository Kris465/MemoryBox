def find_character_by_name():
    characters = ['Эльза', 'Анна', 'Олаф', 'кристоф']

    part_name = input("Введите часть имени персонажа: ")
    found_characters = [char for char in characters if part_name in char]
    if found_characters:
        print("Найдены персонажи: ", ", ".join(found_characters))
    else:
        print("Персонажи не найдены.")


find_character_by_name()
