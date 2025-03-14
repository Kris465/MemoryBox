k = int(input("Введите количество чисел (k): "))

numbers = []

for i in range(k):
    number = int(input(f"Введите число {i + 1}: "))
    numbers.append(number)


last_negative_index = -1


for i in range(k):
    if numbers[i] < 0:
        last_negative_index = i + 1


print(f"Номер последнего отрицательного числа: {last_negative_index}")
