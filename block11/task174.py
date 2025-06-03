def move_last_to_k(arr, k):
    if not arr or k >= len(arr) - 1 or k < 0:
        print("Ошибка: неверное значение k")
        return arr

    last = arr.pop()
    arr.insert(k, last)
    return arr
