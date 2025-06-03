def move_s_to_k(arr, s, k):
    if s < 0 or k < 0 or s >= len(arr) or k >= len(arr) or s <= k:
        raise IndexError("Неправильные значения s и k. Убедитесь, что s > k и находятся в пределах массива.")

    element = arr[s]
    arr.pop(s)

    arr.insert(k, element)

    return arr


arr = [1, 2, 3, 4, 5]
s = 4
k = 2
new_arr = move_s_to_k(arr, s, k)
print(new_arr)

