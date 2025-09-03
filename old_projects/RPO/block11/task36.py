array = [12, -5, 0, 150, 99, -20, 200, 50, 100, -1]

print("Неотрицательные элементы:")
for element in array:
    if element >= 0:
        print(element)

print("\nЭлементы, не превышающие 100:")
for element in array:
    if element <= 100:
        print(element)
