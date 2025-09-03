import numpy as np
from scipy.integrate import quad

def f(x):
    return 0.5 * x + 1

area_under_curve, _ = quad(f, 0, 2)

area_rectangle = 2 * 2

area_figure = area_under_curve - area_rectangle

print(f"Приближенная площадь фигуры: {area_figure:.4f}")
