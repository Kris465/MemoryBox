def process_array(arr):
    has_negative = any(x < 0 for x in arr)
    if not has_negative:
        print("В массиве нет отрицательных чисел.")
        return

    first_neg_index = next(i for i, x in enumerate(arr) if x < 0)
    print(f"а) Первый отрицательный элемент имеет индекс {first_neg_index}")
    print("Элементы, следующие за ним:", arr[first_neg_index+1:])

    last_neg_index = len(arr) - 1 - next(i for i, x in enumerate(reversed(arr)) if x < 0)
    print(f"\nб) Последний отрицательный элемент имеет индекс {last_neg_index}")
    print("Элементы слева от него:", arr[:last_neg_index])


array = [list(map(int, input("Введите массив: ").split()))]
process_array(array)
