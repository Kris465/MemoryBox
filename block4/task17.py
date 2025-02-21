import math


def circle(circle_area, triangel_area):
    r = math.sqrt(circle_area / math.pi)
    h = math.sqrt(3) / 2 * (2 * math.sqrt(triangel_area / (math.sqrt(3) / 4)))\
        ** (1/2)
    r_in = h / 3
    return r <= r_in


def triangel(circle_area, triangel_area):
    R = math.sqrt(circle_area / math.pi)
    a = math.sqrt(triangel_area / (math.sqrt(3) / 4))
    r_circle = a / math.sqrt(3)
    return R >= r_circle


circle_area = int(input('Введите радиус: '))
triangel_area = int(input('Введите сторону трегольника: '))

print('круг поместиться в треугольнике', circle(circle_area, triangel_area))
print('треугольник поместиться в круге', triangel(circle_area, triangel_area))
