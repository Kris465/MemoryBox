def dictionary_of_magic_creatures():
    magic_creatures = {}
    name = ""
    while name != 'exit':
        name = input("Введите имя волшебного существа: ")
        feature = input("Введите особенность волшебного существа: ")
        magic_creatures.update({name: feature})

    return magic_creatures


print(dictionary_of_magic_creatures())
