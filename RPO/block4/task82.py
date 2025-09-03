num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
num3 = int(input("Введите число: "))
num4 = int(input("Введите число: "))
a = 0
if num1 % 2 == 0:
    a += 1
if num2 % 2 == 0:
    a += 1
if num3 % 2 == 0:
    a += 1
if num4 % 2 == 0:
    a += 1
print("Чётных чисел: ", a)
