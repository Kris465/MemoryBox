import math


def max_avg_pair(pairs):
    averages = [(a + b) / 2 for a, b in pairs]
    max_avg = max(averages)
    last_index = len(averages) - 1 - averages[::-1].index(max_avg)
    return last_index + 1


pairs = [(3, 5), (7, 2), (4, 6), (1, 8)]
result = max_avg_pair(pairs)
print(f"Пара с максимальным средним арифметическим: №{result}")


def min_geom_pair(pairs):
    geometrics = [math.sqrt(a * b) for a, b in pairs]
    min_geom = min(geometrics)
    first_index = geometrics.index(min_geom)
    return first_index + 1


pairs = [(3, 5), (7, 2), (4, 6), (1, 8)]
result = min_geom_pair(pairs)
print(f"Пара с минимальным средним геометрическим: №{result}")
