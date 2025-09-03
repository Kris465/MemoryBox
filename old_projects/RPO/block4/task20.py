m = int(input("Введите число: "))
n = int(input("Введите второе число: "))

a = m / n
if m % n == 0:
    print({a})
else:
    print(f'{m} на {n} не делится')
