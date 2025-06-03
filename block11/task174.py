def move_last_to_k(arr, k):
    if k < 0 or k >= len(arr):
        raise IndexError("k должен быть в пределах от 0 до длины массива - 1.")

    last_element = arr[-1]
    arr.pop()

    arr.insert(k, last_element)

    return arr


arr = [1, 2, 3, 4, 5]
k = 2
new_arr = move_last_to_k(arr, k)
print(new_arr)

