yn = int(input("Введите число n: "))
x = int(input("Введите число x: "))
e = int(input("Введите число e: "))
if abs((yn ** 2) - ((yn - 1) ** 2) < e):
    print(0.5 * ((yn - 1) + (x / ((yn - 1) - 1) )))
else:
    print("Ошибка")