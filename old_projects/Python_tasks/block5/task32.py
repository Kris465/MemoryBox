n = int(input("Введите число: "))
summa = 0

for i in range(1, n + 1):
    summa += 1 / i

print(f"Сумма: {summa}")
