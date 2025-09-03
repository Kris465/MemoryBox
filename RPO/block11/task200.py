def print_elements_after_n(arr, n):

    for i in range(len(arr)):
        if arr[i] > n:

            print("Следующие элементы:", *arr[i+1:])
            return

    print("Нет элементов больших", n)


array = [1, 3, 5, 8, 10]
number = 6
print_elements_after_n(array, number)
