a = [5, 3, 8, 1, 2]

for i in range(len(a) - 1):
    if a[i + 1] < a[i]:
        a[i], a[i + 1] = a[i + 1], a[i]

print("Последний элемент:", a[-1])
