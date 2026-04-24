def f(y):
    if y > 2:
        return 2
    elif 0 < y <= 1:
        return 0
    else:
        return -3 * y

    y = float(input("Введите значение y: "))
    result = f(y)
    print(f"Значение функции f(y) при y={y} равно {result}")
