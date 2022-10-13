# 2. Найти максимальное из пяти чисел

lst = []
# lst = [int(i) for i in input().split()]
for i in range(5):
    lst.append(int(input("Input number: ")))

max_ = 0
for elem in lst:
    if elem > max_:
        max_ = elem

# print(max(lst))

print(lst)
print(max_)