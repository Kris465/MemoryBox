arr = [5, 2, 8, 1, 9, 3, 6, 4, 7]


if arr:
    max_val = max(arr)
    max_index = arr.index(max_val)
    arr.pop(max_index)
    print("После удаления максимума:", arr)
else:
    print("Массив пуст!")


if arr:
    min_val = min(arr)
    min_index = arr.index(min_val)
    arr.pop(min_index)
    print("После удаления минимума:", arr)
else:
    print("Массив пуст!")
