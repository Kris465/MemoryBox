arr = [3, -2, 5, 8, -1, 4, 10, 7]

neg_indices = [i for i, x in enumerate(arr) if x < 0]

if neg_indices:
    arr.pop(neg_indices[0])
    print("После удаления первого отрицательного:", arr)
else:
    print("Нет отрицательных элементов.")

even_indices = [i for i, x in enumerate(arr) if x % 2 == 0]

if even_indices:
    arr.pop(even_indices[-1])
    print("После удаления последнего чётного:", arr)
else:
    print("Нет чётных элементов.")
