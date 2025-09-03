import random

# Генерация массивов
array_a = [random.random() for _ in range(15)]
array_b = [random.uniform(22, 23) for _ in range(15)]
array_v = [random.uniform(0, 10) for _ in range(15)]
array_g = [random.uniform(-50, 50) for _ in range(15)]
array_d = [random.randint(0, 10) for _ in range(15)]

# Вывод результатов
print("Массив вещественных чисел в диапазоне от 0 до 1:")
print(array_a)

print("\nМассив вещественных чисел в диапазоне от 22 до 23:")
print(array_b)

print("\nМассив вещественных чисел в диапазоне от 0 до 10:")
print(array_v)

print("\nМассив вещественных чисел в диапазоне от -50 до 50:")
print(array_g)

print("\nМассив целых чисел в диапазоне от 0 до 10:")
print(array_d)
