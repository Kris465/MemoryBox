arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


arr[2:9] = arr[2:9][::-1]
print("а)", arr)


k = int(input("Введите k (k < s): "))  # 3
s = int(input("Введите s (s > k): "))  # 10
arr[k : s-1] = arr[k : s-1][::-1]
print("б)", arr)


max_val = max(arr)
min_val = min(arr)
index_max = arr.index(max_val)
index_min = len(arr) - 1 - arr[::-1].index(min_val)

start = min(index_max, index_min)
end = max(index_max, index_min) + 1


arr[start : end] = arr[start : end][::-1]
print("в)", arr)
