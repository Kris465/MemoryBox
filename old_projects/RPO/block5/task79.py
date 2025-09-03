import numpy as np


def f(x):
    return 0.3*x - 1**2 + 4


a = (1 - 3)/0.3


b = (3 - 3)/0.3


N = 1000


h = (b - a) / N


x = np.linspace(a, b, N+1)
y = f(x)


area = h/2 * np.sum(y[:-1] + y[1:])

print(f"Приблизительная площадь фигуры: {area}")
