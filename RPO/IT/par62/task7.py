import random


def count_second_last_digit_even(size):
    array = [random.randint(1000, 2000) for _ in range(size)]
    even_count = sum(1 for x in array if (x // 10) % 10 % 2 == 0)
    return array, even_count


# Ввод данных
n = int(input("Введите количество элементов: "))


# Заполнение массива и подсчет
result_array, even_count = count_second_last_digit_even(n)
print("Случайные числа:", result_array)
print("Количество элементов с четной второй цифрой с конца:", even_count)
