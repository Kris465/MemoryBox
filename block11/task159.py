def insert_after_second(arr):
    if len(arr) >= 2:
        arr.insert(2, 10)
    else:
        arr.append(10)
    return arr


arr1 = [1, 2, 3, 4]
print(insert_after_second(arr1))

arr2 = [5]
print(insert_after_second(arr2))
