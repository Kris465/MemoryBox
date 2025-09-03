from math import sqrt
first = int(input('Введите первое число: '))
second = int(input("Введите второе число: "))


if sqrt(second) < first:
    second = second * 5


print(f'Второе число: {second}')
