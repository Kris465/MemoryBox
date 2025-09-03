import math


def largest_square_diagonal(areas):
    max_area = max(areas)
    return math.sqrt(2 * max_area)


areas = [25, 36, 16, 49]
diagonal = largest_square_diagonal(areas)
print(f"Длина диагонали самого большого квадрата: {diagonal:.2f}")
