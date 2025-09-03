# Инициализация последовательности
sequence = [1.2, 3.5, -2.1, 4.0, 5.6, 7.8, 0.0, -1.0, 9.3, 10.1, 2.5, 3.1, 4.4, 5.7, 6.9]

# Флаг для проверки наличия отрицательных чисел
found_negative = False
first_negative_index = -1

# Поиск первого отрицательного числа
for index in range(len(sequence)):
    if sequence[index] < 0:
        found_negative = True
        first_negative_index = index + 1  # Порядковый номер (начиная с 1)
        break

# Вывод результата
if found_negative:
    print(f"Первое отрицательное число найдено на позиции: {first_negative_index}")
else:
    print("Отрицательных чисел в последовательности нет.")
