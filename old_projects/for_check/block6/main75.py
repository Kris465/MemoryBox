from collections import Counter

# Пример последовательности
sequence_a = [0, 1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 33]

# Подсчет костей
bones_count_a = Counter((num // 10, num % 10) for num in sequence_a)

# Проверка условий
valid_a = all(count <= 1 for count in bones_count_a.values()) and all(num % 10 <= 6 for num in sequence_a)

print("Случай (а):", "Соответствует" if valid_a else "Не соответствует")


# Пример последовательности
sequence_b = [0, 1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 33]

# Подсчет костей с учетом обоих чисел
bones_count_b = Counter((min(num // 10, num % 10), max(num // 10, num % 10)) for num in sequence_b)

# Проверка условий
valid_b = all(count <= 1 for count in bones_count_b.values()) and all(num // 10 <= 6 and num % 10 <= 6 for num in sequence_b)

print("Случай (б):", "Соответствует" if valid_b else "Не соответствует")
