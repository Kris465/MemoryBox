from random import randint


def find_indices_of_x(arr, x):
    indices = [i for i, value in enumerate(arr) if value == x]
    return indices


array = [randint(0, 4) for _ in range(20)]
x = int(input("Введите значение X от 0 до 4): "))
print("Массив:", array)
print("Индексы элементов равных X:", find_indices_of_x(array, x))
