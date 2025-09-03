def find_smallest_n():
    sums = {}
    limit = 100
    for a in range(1, limit):
        for b in range(a, limit):
            sum_of_cubes = a**3 + b**3
            if sum_of_cubes not in sums:
                sums[sum_of_cubes] = []
            sums[sum_of_cubes].append((a, b))

    smallest_n = None
    for sum_of_cubes, pairs in sums.items():
        if len(pairs) > 1:
            if smallest_n is None or sum_of_cubes < smallest_n:
                smallest_n = sum_of_cubes

    return smallest_n


result = find_smallest_n()
print("Наименьшее натуральное число n:", result)
