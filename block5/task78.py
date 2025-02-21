import numpy as np


def sin_integral(a, b, n):

    x = np.linspace(a, b, n + 1)
    y = np.sin(x)
    dx = (b - a) / n
    area = np.sum(y[:-1]) * dx

    return area


result = sin_integral(0, np.pi/2, 10000)
print(f"Приближенная площадь под синусоидой: {result}")
