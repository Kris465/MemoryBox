def count_elements_greater_then_others_sum(arr):
    total_sum = sum(arr)
    count = 0
    indices = []

    for i in range(len(arr)):
        if arr(i) > (total_sum - arr[i]):
            count += 1
            indices.append(i)

    print("Колличество элементов: {count}")
    print("Их индексы: {indices}")
