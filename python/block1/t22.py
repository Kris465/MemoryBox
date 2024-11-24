def func_x(x):
    y = 7 * x * x - 3 * x + 6
    return y


def func_a(a):
    x = 12 * a * a + 7 * a - 16
    return x


x = int(input("Введите число x: "))
print(f"a)7 * x * x - 3 * x + 6 = {func_x(x)}")

a = int(input("Введите число a: "))
print(f"b)12 * a * a + 7 * a - 16 = {func_a(a)}")
