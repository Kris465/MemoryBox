from itertools import takewhile

arr = [5, 5, 5, 3, 2, 1, 5, 4]

count = len(list(takewhile(lambda x: x == arr[0], arr)))
print("Количество одинаковых элементов в начале:", count)


elements_after = arr[count:]
print("Элементы после последнего одинакового:", elements_after)
