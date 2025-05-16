import math


def trapezoid_area(base1, base2, height):
    return ((base1 + base2) * height) / 2


def trapezoid_perimeter(base1, base2, height):
    leg_length = math.sqrt(height**2 + ((base2-base1)/2)**2)
    return base1 + base2 + 2*leg_length


base1_first = float(input("Введите основание 1 первой трапеции: "))
base2_first = float(input("Введите основание 2 первой трапеции: "))
height_first = float(input("Введите высоту первой трапеции: "))


base1_second = float(input("Введите основание 1 второй трапеции: "))
base2_second = float(input("Введите основание 2 второй трапеции: "))
height_second = float(input("Введите высоту второй трапеции: "))


area_first = trapezoid_area(base1_first, base2_first, height_first)
perimeter_first = trapezoid_perimeter(base1_first, base2_first, height_first)

area_second = trapezoid_area(base1_second, base2_second, height_second)
perimeter_second = \
    trapezoid_perimeter(base1_second, base2_second, height_second)


sum_areas = area_first + area_second
sum_perimeters = perimeter_first + perimeter_second


print(f"Площадь первой трапеции: {area_first:.2f}, \
    периметр первой трапеции: {perimeter_first:.2f}")
print(f"Площадь второй трапеции: {area_second:.2f}, \
    периметр второй трапеции: {perimeter_second:.2f}")
print(f"Сумма площадей: {sum_areas:.2f},\
    сумма периметров: {sum_perimeters:.2f}")
