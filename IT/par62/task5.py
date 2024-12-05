# Манираки
import random


def random_permutation_with_first_five(n):
    if n < 5:
        raise ValueError("N должно быть больше или равно 5")
    array = list(range(1, n + 1))
    array.remove(5)
    random.shuffle(array)
    array.insert(0, 5)
    return array


n = int(input("Введите N (N >= 5): "))

result = random_permutation_with_first_five(n)
print("Случайная перестановка с первым элементом равным 5:", result)
