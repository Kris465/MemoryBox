def find_roots(a, b, c):
    D = b**2 - 4*a*c

    if D > 0:
        root1 = (-b + D ** 0.5) / (2 * a)
        root2 = (-b - D ** 0.5) / (2 * a)
        print(f"Уравнение имеет два вещественных корня : {root1} и {root2}.")
    elif D == 0:
        root = b/(2*a)
        print(f"Уравнение имеет один вещестенный корень: {root}")
    else:
        print("Уравнение не имеет вещественных корней. ")


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

find_roots(a, b, c)
