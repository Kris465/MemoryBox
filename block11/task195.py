def process_array(arr):
    first_negative_idx = None
    last_negative_idx = None

    for idx, num in enumerate(arr):
        if num < 0:
            if first_negative_idx is None:
                first_negative_idx = idx
            last_negative_idx = idx

    if first_negative_idx is not None:
        print("Первый отрицательный элемент имеет индекс:", first_negative_idx)

        print("Элементы после первого отрицательного:")
        for elem in arr[first_negative_idx+1:]:
            print(elem)

        print("\nПоследний отрицательный\
            элемент имеет индекс:", last_negative_idx)

        print("Элементы до последнего отрицательного:")
        for elem in arr[:last_negative_idx]:
            print(elem)
    else:
        print("Отрицательных элементов в массиве нет.")


array_input = input("Введите массив вещественных чисел через пробел: ")
numbers = list(map(float, array_input.split()))  # Преобразуем строки в float

process_array(numbers)
