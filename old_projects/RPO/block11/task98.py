array = list(map(int, input("Введите массив: ").split()))

max_sum = sum(array[0:5])
max_start_index = 0

for i in range(len(array) - 4):
    current_sum = sum(array[i:i+5])
    if current_sum > max_sum:
        max_sum = current_sum
        max_start_index = i

max_sequence = array[max_start_index:max_start_index+5]

print(f"Максимальная сумма: {max_sum}")
print(f"Пять соседних элементов: {max_sequence}")
