def insert_after_first_negative(arr, num):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr.insert(i + 1, num)
            return arr
    arr.append(num)
    return arr
