def sort_pokemon():
    pokemons = []
    while True:
        pokemon = input("Введите имя покемона: ")
        if pokemon.lower() == 'стоп':
            break
        pokemons.append(pokemon)
        print("Покемоны в алфавитном порядке")
        for pokemon in pokemons:
            print(pokemon)


sort_pokemon()
