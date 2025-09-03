# Исходный массив целых чисел
array = [12, 35, 40, 23, 50, 61, 70, 83, 90, 105]

# а) Все четные элементы
print("Четные элементы:")
for element in array:
    if element % 2 == 0:
        print(element)

# б) Все элементы, оканчивающиеся нулем
print("\nЭлементы, оканчивающиеся нулем:")
for element in array:
    if element % 10 == 0:
        print(element)
