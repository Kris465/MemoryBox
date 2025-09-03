rainfall = [10, 5, 0, 12, 8, 7, 3, 0, 4, 6,
            9, 2, 11, 4, 5, 7, 3, 8, 6, 2,
            9, 1, 4, 5, 6, 3, 2, 8, 7, 4]


if len(rainfall) != 30:
    print("Длина массива должна быть равна 30.")
else:

    first_decade = sum(rainfall[0:10])
    second_decade = sum(rainfall[10:20])
    third_decade = sum(rainfall[20:30])

    print(f"Общее количество осадков за первую декаду: {first_decade}")
    print(f"Общее количество осадков за вторую декаду: {second_decade}")
    print(f"Общее количество осадков за третью декаду: {third_decade}")
