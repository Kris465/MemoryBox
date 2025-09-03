n = int(input("Введите количество чисел: "))
sum_odd = 0

for _ in range(n):
    num = float(input("Введите число: "))
    if num % 2 != 1:
        break
    sum_odd += num

print(sum_odd)
