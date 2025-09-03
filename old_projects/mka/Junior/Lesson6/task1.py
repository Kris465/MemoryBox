def dictionary_of_heroes():
    superheroes = {}
    name = ""
    while name != 'exit':
        name = input("Введите имя супергероя: ")
        ability = input("Введите способность супергероя: ")
        superheroes.update({name: ability})

    return superheroes


print(dictionary_of_heroes())
