def move_s_to_k(arr, s, k):
    if s >= k or k >= len(arr) or s < 0:
        return arr

    element = arr[s]

    for i in range(s, k):
        arr[i] = arr[i + 1]

    arr[k] = element

    return arr


arr = [10, 20, 30, 40, 50, 60]
s, k = 1, 4
print("До:", arr)
move_s_to_k(arr, s, k)
print("После:", arr)
