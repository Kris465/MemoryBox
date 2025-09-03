# Ввод массива целых чисел через пробел
array = list(map(int, input("Введите целые числа через пробел: ").split()))

# Подсчет чётных элементов
even_count = sum(1 for x in array if x % 2 == 0)

# Подсчет элементов, оканчивающихся на 5
ending_5_count = sum(1 for x in array if abs(x) % 10 == 5)

# Вывод результатов
print("Чётных элементов:", even_count)
print("Элементов, оканчивающихся на 5:", ending_5_count)
