import random


def average_of_numbers(size):
    array = [random.randint(0, 100) for _ in range(size)]
    less_than_50 = [x for x in array if x < 50]
    greater_equal_50 = [x for x in array if x >= 50]

    avg_less_than_50 = sum(less_than_50) / len(less_than_50) if less_than_50 else None
    avg_greater_equal_50 = sum(greater_equal_50) / len(greater_equal_50) if greater_equal_50 else None

    return array, avg_less_than_50, avg_greater_equal_50


# Ввод данных
n = int(input("Введите количество элементов: "))


# Заполнение массива и подсчет средних значений
result_array, avg_less_than_50, avg_greater_equal_50 = average_of_numbers(n)
print("Случайные числа:", result_array)
print("Среднее значение элементов <50:", avg_less_than_50)
print("Среднее значение элементов >=50:", avg_greater_equal_50)
