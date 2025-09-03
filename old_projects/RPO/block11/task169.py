def move_first_to_last(arr):
    if len(arr) <= 1:
        return arr

    first_element = arr[0]

    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]

    arr[-1] = first_element

    return arr


arr = [list(map(int, input("ВВедите массив")))]
print("До:", arr)
move_first_to_last(arr)
print("После:", arr)
