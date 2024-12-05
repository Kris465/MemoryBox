def dictionary_of_sportsmen():
    sportsmen = {}
    name = ""
    while name != 'exit':
        name = input("Введите имя спортсмена: ")
        aim = input("Введите достижение спортсмена: ")
        sportsmen.update({name: aim})

    return sportsmen


print(dictionary_of_sportsmen())
