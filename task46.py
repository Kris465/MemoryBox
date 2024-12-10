a = int(input("Введите длину первой стороны: "))
b = int(input("Введите длину второй стороны: "))
c = int(input("Введите длину третьей стороны: "))

volume = a * b * c

side_surface_area = 2 * (a * c + b * c)

print("Объем параллепипеда: ", volume)
print("Площадь боковой поверхности: ", side_surface_area)
