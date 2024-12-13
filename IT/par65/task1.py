def sort_and_find(arr, target):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return [x for x in arr if x == target]


arr = [34, 23, 12, 45, 56, 78, 34, 23]
target = 34
print(sort_and_find(arr, target))
