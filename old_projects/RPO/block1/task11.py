import random

choice = input("Хотите ввести числа вручную? (да/нет): ").lower()

if choice == 'да':
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    num3 = int(input("Введите третье число: "))
    num4 = int(input("Введите четвертое число: "))
else:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)


print(num1)
print(num2)
print(num3)
print(num4)
