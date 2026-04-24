m = int(input("Введите количество элементов последовательности: "))
sequence = input("Введите последовательность (0 и 1): ")
min_length = float('inf')
current_length = 0

for char in sequence:
    if char == '0':
        current_length += 1
    else:
        if current_length > 0:
            min_length = min(min_length, current_length)
        current_length = 0

if current_length > 0:
    min_length = min(min_length, current_length)

if min_length == float('inf'):
    print("В последовательности нет нулей.")
else:
    print(f"Наименьшая длина отрезка из нулей: {min_length}.")
