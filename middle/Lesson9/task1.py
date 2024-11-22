def superhero_powers():
    superheroes = []
    while True:
        name = input("Введите имя супергероя или 'стоп' для завершения: ")
        if name.lower() == 'стоп':
            break
        powers = input("Введите суперсилы (через запятую): ").split()
        powers = [power.strip() for power in powers]
        superheroes.append((name, powers))

        superheroes.sort(key=lambda x: len(x[1]), reverse=True)
        print("\nИнформация о супергероях:")
        for hero in superheroes:
            print(f"Супергерой {hero[0]} имеет следующие суперсилы: {', '.join(hero[1])}")


superhero_powers()
