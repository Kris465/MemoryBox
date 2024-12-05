def dictionary_of_zoo():
    zoo = {}
    name = ""
    while name != 'exit':
        name = input("Введите имя спортсмена: ")
        features = input("Введите достижение спортсмена: ")
        zoo.update({name: features})

    return zoo


print(dictionary_of_zoo())
