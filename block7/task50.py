def find_last_index_greater_than_100(arr, n):
    for i in range(n - 1, -1, -1):
        if arr[i] > 100:
            return i + 1
    return None


arr = [120, 50, 150, 80, 110]
n = len(arr)
result = find_last_index_greater_than_100(arr, n)
print(result)
