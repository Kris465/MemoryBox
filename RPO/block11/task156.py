def remove_range(arr, n1, n2):
    return arr[:n1-1] + arr[n2:]


arr = [10, 20, 30, 40, 50, 60, 70]
n1, n2 = 2, 4
result = remove_range(arr, n1, n2)
print(result)
