from math import sqrt

a = int(input("Введите число: "))
b = int(input("Введите число: "))

mean_arithmetic = (abs(a) + abs(b)) / 2
mean_geometric = sqrt(abs(a) * abs(b))

print("Среднее арифметическое модулей: ", mean_arithmetic)
print("Среднее геометрическое модулей: ", mean_geometric)
