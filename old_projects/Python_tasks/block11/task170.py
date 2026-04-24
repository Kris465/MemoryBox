def move_first_to_kth(arr, k):
    if len(arr) <= 1 or k <= 0 or k >= len(arr):
        return arr

    first = arr[0]

    for i in range(k):
        arr[i] = arr[i + 1]

    arr[k] = first

    return arr


arr = [10, 20, 30, 40, 50]
k = 2
print("До:", arr)
move_first_to_kth(arr, k)
print("После:", arr)
