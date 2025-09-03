def fix_sorted_array(arr):

    if len(arr) == 0:
        print("Массив пустой")
        return arr

    last = arr[-1]

    arr.pop()

    i = 0
    while i < len(arr) and arr[i] <= last:
        i += 1

    arr.insert(i, last)

    return arr
