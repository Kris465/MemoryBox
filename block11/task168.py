def insert_between_same_sign(arr, n):
    i = 1
    while i < len(arr):
        if (arr[i-1] * arr[i] > 0):
            arr.insert(i, n)
            i += 1
        i += 1
    return arr


arr = [1, 2, -3, -4, 5, -6]
n = 0
print(insert_between_same_sign(arr, n))
