from itertools import count

list1 = [1, 2, 3, 3, 3, 3, 5, 7, 8, 9, 5, 5, 5, 7]

list2 = []

for i in range(len(list1) - 1):
    if list1.count(i) == 1:
        list2.append(i)
print(list2)