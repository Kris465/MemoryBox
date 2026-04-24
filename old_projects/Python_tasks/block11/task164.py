def insert_before_multiples(arr, x, a):
    i = 0
    while i < len(arr):
        if arr[i] % a == 0:
            arr.insert(i, x)
            i += 1
        i += 1
    return arr


arr = [10, 3, 5, 20, 6]
x = 0
a = 5
print(insert_before_multiples(arr, x, a))
