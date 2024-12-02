import random


def random_permutation(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    return array


# Ввод данных
n = int(input("Введите N (количество элементов): "))


# Заполнение массива
result = random_permutation(n)
print("Случайная перестановка:", result)
