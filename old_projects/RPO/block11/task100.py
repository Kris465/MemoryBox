array = [3, 5, 7, 2, 5, 9]


if len(array) != len(set(array)):
    print("В массиве есть одинаковые элементы.")
else:
    print("Все элементы в массиве уникальны.")
