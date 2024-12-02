import random


def random_permutation_with_first_five(n):
    if n < 5:
        raise ValueError("N должно быть больше или равно 5")

    array = list(range(1, n + 1))
    array.remove(5)  # Удаляем 5 из списка
    random.shuffle(array)  # Перемешиваем оставшиеся элементы
    array.insert(0, 5)  # Вставляем 5 на первое место
    return array


# Ввод данных
n = int(input("Введите N (N >= 5): "))


# Заполнение массива
result = random_permutation_with_first_five(n)
print("Случайная перестановка с первым элементом равным 5:", result)
