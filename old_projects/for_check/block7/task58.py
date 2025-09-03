import math


def smallest_circle_radius(areas):
    min_area = min(areas)
    return math.sqrt(min_area / math.pi)


areas = [50, 30, 80, 20]
radius = smallest_circle_radius(areas)
print(f"Радиус самого маленького круга: {radius:.2f}")
