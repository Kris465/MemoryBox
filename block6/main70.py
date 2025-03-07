def is_increasing(sequence):

    if len(sequence) < 2:
        return False, 0  # Недостаточно элементов для сравнения

    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i+1]:
            return False, i + 2  # i + 2, так как нумерация с 1

    return True, 0


# Пример использования:
sequence1 = [1, 2, 3, 4, 10000]
result1, index1 = is_increasing(sequence1)
print(f"Последовательность {sequence1} упорядочена по возрастанию: {result1}, индекс нарушения: {index1}")

sequence2 = [1, 3, 2, 4, 10000]
result2, index2 = is_increasing(sequence2)
print(f"Последовательность {sequence2} упорядочена по возрастанию: {result2}, индекс нарушения: {index2}")

sequence3 = [10, 5, 1, 10000]
result3, index3 = is_increasing(sequence3)
print(f"Последовательность {sequence3} упорядочена по возрастанию: {result3}, индекс нарушения: {index3}")

sequence4 = [10000] # пример с одним элементом (не должно быть больше 2)
result4, index4 = is_increasing(sequence4)
print(f"Последовательность {sequence4} упорядочена по возрастанию: {result4}, индекс нарушения: {index4}")
