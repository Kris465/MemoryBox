arr = [1, 0, 2, 0, 3, 0, 4]
reversed_index = arr[::-1].index(0)
last_zero_index = len(arr) - 1 - reversed_index
result = arr[:last_zero_index] + arr[last_zero_index + 1:]
print(result)
