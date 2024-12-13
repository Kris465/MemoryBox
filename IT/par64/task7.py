def find_max_duplicate(arr):
    count = []

    for num in arr:
        count[num] = count.get(num, 0) + 1

    max_duplicate = None
    for num, cnt in count.items():
        if cnt > 1:
            if max_duplicate is None or num > max_duplicate:
                max_duplicate = num

    return max_duplicate


arr = [3, 5, 1, 3, 7, 8, 5, 2, 1]
result = find_max_duplicate(arr)

if result is not None:
    print("Максимальное число, встречающееся несколько раз:", result)
else:
    print("Нет чисел, которые встречаются несколько раз.")
