def has_real_roots(a, b, c):
    """проверка наличия вещественных корней в квадратном уравнении."""
    discriminant = b**2 - 4*a*c
    return discriminant >= 0


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

equation1 = has_real_roots(a, b, c)
equation2 = has_real_roots(b, a, c)
equation3 = has_real_roots(c, a, b)

count_real_roots = sum([equation1, equation2, equation3])


print(f"Коли квадратных уравнений с вещественными корнями: {count_real_roots}")
