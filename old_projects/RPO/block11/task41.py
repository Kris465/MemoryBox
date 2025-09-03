# Исходный массив целых чисел
array = [12, 7, 4, 9, 20, 33, 8, 15]

# Вывод четных элементов
print("Четные элементы:")
for element in array:
    if element % 2 == 0:
        print(element)

# Вывод нечетных элементов
print("\nНечетные элементы:")
for element in array:
    if element % 2 != 0:
        print(element)
