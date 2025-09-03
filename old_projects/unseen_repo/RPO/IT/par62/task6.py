import random


def random_numbers_and_count_even_odd(size):
    array = [random.randint(20, 100) for _ in range(size)]
    even_count = sum(1 for x in array if x % 2 == 0)
    odd_count = size - even_count
    return array, even_count, odd_count


# Ввод данных
n = int(input("Введите количество элементов: "))

# Заполнение массива и подсчет четных и нечетных чисел
result_array, even_count, odd_count = random_numbers_and_count_even_odd(n)
print("Случайные числа:", result_array)
print("Количество четных чисел:", even_count)
print("Количество нечетных чисел:", odd_count)
