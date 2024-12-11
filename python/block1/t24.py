from math import sqrt, sin, radians

a = int(input("Введите значение а: "))
x = int(input("Введите значение x: "))

print("a) x = sqrt(2 * a + sin(radians(abs(3 * a)))) / 3.56 =",
      f"{round(sqrt(2 * a + sin(radians(abs(3 * a)))) / 3.56, 2)}")

print("б) y = sin(radians(3.2 + sqrt(1 + x) / abs(5 * x))) =",
      f"{round(sin(radians(3.2 + sqrt(1 + x) / abs(5 * x))), 2)}")
