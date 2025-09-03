def is_decreasing(sequence):

    if len(sequence) < 2:
        return False, 0  # Недостаточно элементов для сравнения

    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:
            return False, i + 2 # Индекс начинается с 1.
    return True, 0

# Пример использования:
sequence1 = [180, 175, 170, 165, 160]
result1, index1 = is_decreasing(sequence1)
print(f"Последовательность {sequence1} упорядочена по убыванию: {result1}, индекс нарушения: {index1}")

sequence2 = [180, 175, 170, 160, 165]
result2, index2 = is_decreasing(sequence2)
print(f"Последовательность {sequence2} упорядочена по убыванию: {result2}, индекс нарушения: {index2}")

sequence3 = [180, 175, 170, 160, 160] # Пример с одинаковыми значениями
result3, index3 = is_decreasing(sequence3)
print(f"Последовательность {sequence3} упорядочена по убыванию: {result3}, индекс нарушения: {index3}")

sequence4 = [160, 165, 170, 175, 180] # Пример возрастающей последовательности
result4, index4 = is_decreasing(sequence4)
print(f"Последовательность {sequence4} упорядочена по убыванию: {result4}, индекс нарушения: {index4}")
