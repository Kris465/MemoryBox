def find_partitions(n, max_num=None):
    if max_num is None:
        max_num = n

    if n == 0:
        return [[]]

    partitions = []

    for i in range(1, max_num + 1):
        if i <= n:
            for partition in find_partitions(n - i, i):
                partitions.append([i] + partition)

    return partitions


# Пример использования
N = int(input("Введите число N для разложения: "))
partitions = find_partitions(N)
for partition in partitions:
    print(" + ".join(map(str, partition)))
