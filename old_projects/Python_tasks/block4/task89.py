from math import sin, radians
x = int(input("Введите число x: "))
if sin(radians(x)) < 0:
    k = x ** 2
elif x >= 0:
    k = abs(x)
if k < x:
    f = k * x
elif k >= x:
    f = k + x
print("f =", f)
