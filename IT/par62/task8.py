import random


def average_of_numbers(size):
    array = [random.randint(0, 100) for _ in range(size)]
    less_then_50 = [x for x in array if x >= 50]
    greater_equal_50 = [x for x in array if x < 50]
    avg_less_then_50 = sum(less_then_50) / len(less_then_50) if less_then_50 else None 
    avg_greater_equal_50 = sum(greater_equal_50) / len(greater_equal_50) if greater_equal_50 else None

    return array, avg_less_then_50, avg_greater_equal_50


#вывод данных
n = int(input("Введите количество элементов:"))

#заполнение массива и подсчет средних значений
result_arrey, avg_less_then_50, avg_greater_aquel_50 = average_of_numbers(n)
print("случайные числа:", result_arrey)
print("среднее значение элементов <50:", avg_less_then_50)
print("среднее значение элементов >=50:", avg_greater_aquel_50)
