arr = [1, 4, 5, 6, 7, 8, 9, 0]
i = 0
c = 0
a = len(arr)
while a > 0:
    i += arr[a - 1]
    c += 1
    a -= 1
print(i)
print(c)
