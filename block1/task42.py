from math import sqrt, sin, radians
e = int(input("Введите число e: "))
h = int(input("Введите число h: "))
g = int(input("Введите число g: "))
f = int(input("Введите число f: "))

a = (e + (f / 2)) / 3
b = abs(h ** 2 - g)
c = sqrt((g - h) ** 2 - 3 * sin(radians(e)))

print("а = ", a)
print("b = ", b)
print("c = ", c)
