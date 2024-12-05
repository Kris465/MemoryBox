def count_max_elements(arr):
    if not arr:
        return 0

    max_value = arr[0]
    count = 1

    for num in arr[1:]:
        if num > max_value:
            max_value = num
            count = 1
        elif num == max_value:
            count += 1

    return count


array = list(map(int, input("Введите массив чисел через пробел: ").split()))
print("Количество элементов с максимальным значением:",
      count_max_elements(array))
