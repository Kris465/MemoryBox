from math import sqrt, sin, radians


e = float(input("Введите число e "))
f = float(input("Введите число f "))
g = float(input("Введите число g "))
h = float(input("Введите число h "))


a = ((e + (f / 2)) / abs(3))
b = (abs( h**2 - g))
c = sqrt((g - h)**2 - 3 * sin(radians(e)))

print(a, b, c)
