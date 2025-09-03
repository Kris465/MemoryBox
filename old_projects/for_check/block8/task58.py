def find_smallest_taxicab_number():
    sums_of_cubes = {}

    for a in range(1, 100):
        for b in range(a, 100):
            s = a**3 + b**3
            if s in sums_of_cubes:
                sums_of_cubes[s].append((a, b))
            else:
                sums_of_cubes[s] = [(a, b)]

    for s in sorted(sums_of_cubes.keys()):
        if len(sums_of_cubes[s]) >= 2:
            return s, sums_of_cubes[s]


result, representations = find_smallest_taxicab_number()
print(f"Наименьшее число: {result}")
print("Представления:", representations)
