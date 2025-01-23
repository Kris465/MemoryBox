a = int(input('Введите первое число: '))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
z = 0

if a < b < c:
    z = b + c
    print(f"Сумма наибольших цифр: {z}")

if a < c < b:
    z = c + b
    print(f"Сумма наибольших цифр: {z}")

if b < c < a:
    z = c + a
    print(f"Сумма наибольших цифр: {z}")

if b < a < c:
    z = a + c
    print(f"Сумма наибольших цифр: {z}")

if c < b < a:
    z = b + a
    print(f"Сумма наибольших цифр: {z}")

if c < a < b:
    z = a + b
    print(f"Сумма наибольших цифр: {z}")
