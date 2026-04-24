def find_natural_solutions():
    solutions = set()
    for x in range(1, 31):
        for y in range(x, 31):
            k = 2 ** x + 2 ** y
            if 1 <= k <= 30:
                solutions.add((x, y, k))
    return solutions


solutions = find_natural_solutions()
for solution in solutions:
    print(solution)
