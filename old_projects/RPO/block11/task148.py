def swap_first_neg_last_pos(arr):
    first_neg = None
    for i in range(len(arr)):
        if arr[i] < 0:
            first_neg = i
            break

    last_pos = None
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > 0:
            last_pos = i
            break

    if first_neg is not None and last_pos is not None:
        arr[first_neg], arr[last_pos] = arr[last_pos], arr[first_neg]
        return True
    else:
        return False


arr1 = [1, 2, -3, 4, -5, 6]
if swap_first_neg_last_pos(arr1):
    print("Обмен выполнен:", arr1)
else:
    print("Обмен невозможен")

arr2 = [1, 2, 3, 4]
if swap_first_neg_last_pos(arr2):
    print("Обмен выполнен:", arr2)
else:
    print("Обмен невозможен")

arr3 = [-1, -2, -3]
if swap_first_neg_last_pos(arr3):
    print("Обмен выполнен:", arr3)
else:
    print("Обмен невозможен")

arr4 = [0, 0, 0]
if swap_first_neg_last_pos(arr4):
    print("Обмен выполнен:", arr4)
else:
    print("Обмен невозможен")
