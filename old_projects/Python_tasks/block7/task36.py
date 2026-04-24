
n = int(input("Введите количество чисел: "))


numbers = []
for i in range(n):
    num = float(input(f"Введите число {i + 1}: "))
    numbers.append(num)


count_greater_than_neighbors = 0


for i in range(1, n - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        count_greater_than_neighbors += 1


print(f"Количество чисел, больших своих \
      соседей: {count_greater_than_neighbors}")
