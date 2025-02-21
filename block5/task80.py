import numpy as np


def f(x):
    return np.sqrt(x)


def trapezoidal_rule(a, b, n, func):
    h = (b - a) / n
    s = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        xi = a + i * h
        s += func(xi)
    return h * s


a = 0
b = 2
n = 1000  # Количество интервалов разбиения

# Прямая y = 2
straight_line_value = 2

# Площадь под функцией y = sqrt(x) от 0 до 2
area_under_curve = trapezoidal_rule(a, b, n, f)

# Общая площадь фигуры
total_area = straight_line_value * b - area_under_curve

print("Приблизительная площадь фигуры:", total_area)
