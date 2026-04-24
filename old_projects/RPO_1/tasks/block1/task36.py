from math import pi


outer_radius = int(input("Введите внешний радиус: "))
inner_radius = int(input("Введите внутренний радиус: "))
square = pi * (outer_radius ** 2 - inner_radius ** 2)

print(round(square, 2))
