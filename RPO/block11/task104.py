array = list(map(int, input("Введите массив: ").split()))

group_count = 1 if len(array) > 0 else 0
for i in range(1, len(array)):
    if array[i] != array[i: -1]:
        group_count += 1

distinct_numbers = len(set(array))

print(f"Количество групп одинаковых подряд идущих элементов: {group_count}")
print(f"Количество различных чисел: {distinct_numbers}")
