def is_in_shaded_area(x, y):

    if -2 <= x <= 1 and 0 <= y <= (x + 1) ** 2:
        return True
    if -2 <= x <= 1 and 0 <= y <= x + 2:
        return True
    if -2 <= x <= 1 and 0 <= y <= x ** 0.5:
        return True
    if -2 <= x <= 1 and 0 < y <= 4 / x:
        return True

    return False


x = float(input("Введите число x: "))
y = float(input("Введите число y: "))

if is_in_shaded_area(x, y):
    print(f"Точка ({x}, {y}) находится в заштрихованной области.")
else:
    print(f"Точка ({x}, {y}) не находится в заштрихованной области.")
