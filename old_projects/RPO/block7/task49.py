n = int(input("Введите количество чисел: "))
numbers = []

for i in range(n):
    number = int(input(f"Введите число {i + 1}: "))
    numbers.append(number)

first_index = -1
for i in range(n):
    if numbers[i] == 10:
        first_index = i + 1
        break

if first_index != -1:
    print(f"Номер первого числа, равного 10: {first_index}")
else:
    print("Чисел, равных 10, не найдено.")
