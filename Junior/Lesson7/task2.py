def favourite_superheroes():
    superheroes = []
    while True:
        hero = input("Введите имя супергероя: ")
        if hero.lower() == 'стоп':
            break
        superheroes.append(hero)

    print("Ваши любимые супергерои: ")
    for hero in superheroes:
        print(hero)


favourite_superheroes()
