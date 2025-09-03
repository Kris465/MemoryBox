a = int(input("Введите число а: "))
b = int(input("Введите число б: "))

if a % b == 0:
    print(f"{b} является делителем {a}")
else:
    print(f'{a} на {b} не делится')

if b % a == 0:
    print(f"{a} является делителем {b}")
else:
    print(f'{b} на {a} не делится')
