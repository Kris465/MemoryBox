import random

# Задаем параметры
size = 10  # Размер списков
min_value = 1  # Минимальное значение для случайных чисел
max_value = 100  # Максимальное значение для случайных чисел

# Заполняем два списка случайными числами
list1 = [random.randint(min_value, max_value) for _ in range(size)]
list2 = [random.randint(min_value, max_value) for _ in range(size)]

print("Список 1:", list1)
print("Список 2:", list2)

# 1. Сформировать третий список, содержащий элементы обоих списков
combined_list = list1 + list2
print("Элементы обоих списков:", combined_list)

# 2. Сформировать третий список, содержащий элементы обоих списков без повторений
unique_combined_list = list(set(combined_list))
print("Элементы без повторений:", unique_combined_list)

# 3. Сформировать третий список, содержащий элементы общие для двух списков
common_elements = list(set(list1) & set(list2))
print("Общие элементы:", common_elements)

# 4. Сформировать третий список, содержащий только уникальные элементы каждого из списков
unique_list1 = list(set(list1))
unique_list2 = list(set(list2))
unique_elements = unique_list1 + unique_list2
print("Уникальные элементы каждого списка:", unique_elements)

# 5. Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков
min_max_list1 = [min(list1), max(list1)]
min_max_list2 = [min(list2), max(list2)]
min_max_combined = min_max_list1 + min_max_list2
print("Минимальные и максимальные значения:", min_max_combined)
