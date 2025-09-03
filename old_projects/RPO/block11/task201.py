def print_elements(arr, a):

    idx = None
    for i in range(len(arr)):
        if arr[i] < a:
            idx = i
            break

    if idx is not None:

        before_a = arr[:idx]
        after_first_less_than_a = arr[idx+1:]

        print("Все элементы, большие a:", before_a)
        print("Элементы, следующие за первым меньшим a:",
              after_first_less_than_a)
    else:

        print(f"Все элементы массива больше или равны {a}.")


arr = [10, 8, 6, 5, 3, 1]
a = 4
print_elements(arr, a)
