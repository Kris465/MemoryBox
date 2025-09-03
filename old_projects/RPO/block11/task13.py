my_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

index = int(input("Введите индекс элемента массива: "))

if index < 0 or index >= len(my_array):
    print("Неверный индекс!")
else:
    print(f"Элемент массива по индексу {index}: {my_array[index]}")