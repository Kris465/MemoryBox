# 2. Найти максимальное из пяти чисел

lst = []
for i in range(5):
    lst.append(int(input("Input number: ")))

max_ = 0
for elem in lst:
    if elem > max_:
        max_ = elem

print(lst)
print(max_)