def move_first_k_to_end(arr, k):
    if k <= 0 or k >= len(arr):
        return arr
    return arr[k:] + arr[:k]


m = list(range(1, 29))
k = 5
result = move_first_k_to_end(m, k)
print(result)
