from math import sin, radians

# a
print("Умножить число х на два.")
x = int(input('Введите х: '))
print(2 * x)

# б
print("Посчитать синус градуса угла: ")
gradus = int(input("Введите градусы угла: "))
rads = radians(gradus)
print(round(sin(rads), 2))

# в
print("Возвести число а во вторую степень")
a = int(input("Введите а: "))
print(a * a)

# г
print("Извлечь квадратный корень из числа: ")
number = int(input("Введите число: "))
