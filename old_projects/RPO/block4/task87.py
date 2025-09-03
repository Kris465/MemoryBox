def f(x):
    if x >= 2:
        return 0
    elif 0 < x < 1:
        return x**2
    else:
        return 2


x = float(input("Введите значение x:"))
result = f(x)
print(f"значение функци f={x} при x={x} равно {result}")
