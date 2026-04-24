
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Исходный массив:", arr)


arr[2:9] = arr[2:9][::-1]
print("а) После разворота [2:9]:", arr)


k = int(input("Введите k (k < s): "))
s = int(input("Введите s (s > k): "))

arr[k:s] = arr[k:s][::-1]
print("б) После разворота [k:s]:", arr)


max_val = max(arr)
min_val = min(arr)


index_max = arr.index(max_val)


index_min = len(arr) - 1 - arr[::-1].index(min_val)


start = min(index_max, index_min)
end = max(index_max, index_min) + 1


arr[start:end] = arr[start:end][::-1]

print("в) После разворота между max и последним min:", arr)
