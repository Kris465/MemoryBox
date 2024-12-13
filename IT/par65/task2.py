import random


def binSearch(arr, target):
    a = 0
    b = len(arr) - 1
    if target < arr[a] and target > arr[b]:
        return -1, 0
    if target == arr[a]:
        return 0, 1
    if target == arr[b]:
        return (b, 1)
    counter = 0

    while True:
        if (b-a) <= 1:
            return (-1, counter)
        counter += 1
        c = (a + b) // 2
        if target == arr[c]:
            return (c, counter)
        if arr[c] > target:
            b = c
        else:
            a = c


arr = []
for i in range(33):
    arr += [int(100 * random.random())]

a = int(100 * random.random())
print(str(arr))
print(a)
res = binSearch(arr, a)
print(res)
