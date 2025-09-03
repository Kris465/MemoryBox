grades = list(map(int, input(
    "Введите оценки 22 учеников через пробел: ").split()))

if len(grades) != 22:
    print("Ошибка: необходимо ввести ровно 22 оценки.")
else:
    fives = sum(1 for g in grades if g == 5)
    fours = sum(1 for g in grades if g == 4)
    threes = sum(1 for g in grades if g == 3)
    twos = sum(1 for g in grades if g == 2)

    print("Пятёрок:", fives)
    print("Четвёрок:", fours)
    print("Троек:", threes)
    print("Двоек:", twos)
