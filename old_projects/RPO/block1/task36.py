import math


def ring_area(external_radius, internal_radius):
    if external_radius <= internal_radius:
        raise ValueError("Внешний радиус должен быть больше внутреннего")
    area = math.pi * (external_radius * 2 - internal_radius * 2)
    return area


external_radius = int(input("Введите внешний радиус: "))
internal_radius = int(input("Введите внутренний радиус: "))

try:
    area = ring_area(external_radius, internal_radius)
    print(f"Площадь кольца: {area:.2f}")
except ValueError as e:
    print(e)
