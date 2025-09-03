from math import sin, radians, cos

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
x = int(input("Введите число x: "))
d = int(input("Введите число d: "))
R = 8.31

print(f"a) a / b / c = {round(a / b / c, 2)}")
print(f"б) a * b / c = {round(a * b / c, 2)}")
print(f"в) a / b + c = {round(a / b + c, 2)}")
print(f"г) a + b / c = {round(a + b / c, 2)}")
print(f"д) (a + b) / c = {round((a + b) / c, 2)}")
print(f"е) a + b / b + c = {round(a + b / b + c, 2)}")
print(f"ж) (a + b) / (b + c) = {round((a + b) / (b + c), 2)}")
print(f"з) a / sin(b) = {round(a / sin(radians(b)), 2)}")
print(f"и) 1 / 2 * a * b * sin(rasians(x)) = \
    {round(1 / 2 * a * b * sin(radians(c)), 2)}")
print(f"к) (2 * b * c * cos(radians(a / 2)) / (b + c)) = \
    {round((2 * b * c * cos(radians(a / 2)) / (b + c)), 2)}")
print(f"л) 4 * R * sin(radians(a / 2) * \
        sin(radians(b / 2)) * sin(radians(c / 2))) = \
            {round(4 * R * sin(radians(a / 2) * sin(radians(b / 2)) * sin(
                        radians(c / 2))), 2)}")
print(f"м) (a * x + b) / (c * x + d) = {round((a * x + b) / (c * x + d), 2)}")
print(f"н) (2 * sin(radians(a + b)) / 2 * cos(radians(a - b)) / 2) = \
    {round((2 * sin(radians(a + b)) / 2 * cos(radians(a - b)) / 2), 2)}")
print(f"о) abs(2 * sin(radians(-3 * abs(x / 2))) = \
    {abs(2 * sin(radians(-3 * abs(x / 2))))}")
