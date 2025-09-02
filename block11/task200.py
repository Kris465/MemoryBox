def print_elements_after_n(arr, n):

    for i in range(len(arr)):
        if arr[i] > n:
            # Нашли первый элемент больше n, выводим остальные элементы
            print("Следующие элементы:", *arr[i+1:])
            return

    # Если ни один элемент не оказался больше n
    print("Нет элементов больших", n)


array = [1, 3, 5, 8, 10]
number = 6
print_elements_after_n(array, number)
