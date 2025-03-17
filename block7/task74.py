n = int(input("Введите количество целых чисел: "))
number = []

maximum = float('-inf')
minimum = float('inf')

for _ in range(n):
    num = int(input("Введите число: "))
    number.append(num)
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

count_max = number.count(maximum)
count_min = number.count(minimum)

print(f"Максимальное значение {maximum} встречается {count_max} раз.")
print(f"Минимальное значение {minimum} встречается {count_min} раз.")
