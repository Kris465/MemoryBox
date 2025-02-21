try:
    m1 = int(input("Введите массу первого тела: "))
    v1 = int(input("Введите объём первого тела: "))
    m2 = int(input("Введите массу второго тела: "))
    v2 = int(input("Введите объём второго тела: "))
except ValueError:
    print("Введите число, а не букву(символ)")
try:
    p1 = m1 / v1
    p2 = m2 / v2
    if p1 > p2:
        print(f"Большая плотность у первого тела: {p1}")
    elif p1 < p2:
        print(f"Большая плотность у второго тела: {p2}")
    else:
        print("Они равны")
except NameError:
    print("Ошибка")
