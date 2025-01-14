from math import pi
d = (int(input('введите площадь круга: ')))
a = (int(input('введите площадь квадрата: ')))
diametr = ((d / pi) ** 0.5) * 2
storona = a ** 0.5
diogonali = (2 * (storona ** 2)) ** 0.5
print("а): ")


if diametr <= storona:
    print("круг умещаеться в квадрате")
else:
    print("круг не_умещаеться в квадрате")


print("в): ")


if diametr >= diogonali:
    print("квадрат умещаеться в круге")
else:
    print("квадрат не_умещаеться в круге")
