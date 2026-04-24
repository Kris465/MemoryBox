import math
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

if a == 0:
    print("Уравнение не является квадратичным.")
else:
    D = b ** 2 - 4 * a * c
    print(f"Дискриминант = {D}")

    if D > 0:
        print("У уравнения есть два корня")
    elif D == 0:
        print("У уравнения есть один корень")
    else:
        print("У уравнения нет корней")
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(x1, x2)
    elif D == 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        print(x1)
    else:
        print("У уравнения нет корней")
