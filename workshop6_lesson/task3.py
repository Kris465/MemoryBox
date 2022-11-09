lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 5, 6, 2]
lst1 = [i for i in lst if lst.count(i) == 1]
print(f"Original list: {lst}")
print(f"Unique elements: {lst}")
lst2 = list(set(lst))
print(f"Unique elements in multiplicity: {lst2}")
lst3 = list()
for i in lst:
    if i not in lst3:
        lst3.append(i)
print(f"The list of unique elements: {lst3}")
lst4 = [lst[i] for i in range(len(lst)) if lst[0: i].count(lst[i]) == 0]
print(f"The list of unique elements from the running: {lst4}")