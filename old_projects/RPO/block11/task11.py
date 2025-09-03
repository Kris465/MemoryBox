import random

# Диапазон возможных чисел
min_val = 1
max_val = 100

# Выбор 20 уникальных случайных чисел из диапазона
unique_random_numbers = random.sample(range(min_val, max_val + 1), 20)

# Выводим массив уникальных случайных чисел
print(unique_random_numbers)
