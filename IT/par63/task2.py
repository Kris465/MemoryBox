n = int(input("Введите количество элементов в массиве:"))
a = []

for i in range(n):
    a.append(int(input()))

max_elem = max(a)
count_max_elem = a.count(max_elem)
print(f'Количество максимальных элементов в масиве:{count_max_elem}')
