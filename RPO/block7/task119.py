# Пример данных
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Нахождение максимального и минимального числа
max_num = max(numbers)
min_num = min(numbers)

# Проверка условия
is_difference_less_than_25 = (max_num - min_num) <= 25
print(f"Разница между максимальным и минимальным числом не\
    превышает 25: {is_difference_less_than_25}")
