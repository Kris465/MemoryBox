def recursive_max(arr):

    if len(arr) == 1:
        return arr[0]
    else:

        last_element = arr[-1]
        max_rest = recursive_max(arr[:-1])
        return max(last_element, max_rest)


array = [3, 5, 1, 8, 4, 9, 2]
max_value = recursive_max(array)
print(f"Максимальный элемент массива: {max_value}")
