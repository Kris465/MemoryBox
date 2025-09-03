array = [12, -5, 0, -3, 7, -1, 0, -8]

print("Неотрицательные элементы:")
for element in array:
    if element >= 0:
        print(element)

print("\nОтрицательные элементы:")
for element in array:
    if element < 0:
        print(element)