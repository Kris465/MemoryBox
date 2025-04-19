def find_x(target):
    for A in range(1, 10):
        for B in range(0, 10):
            for C in range(0, 10):
                if 11 * A + 100 * B + 10 * C == target:
                    return A * 1000 + B * 100 + C * 10 + A
    return None

result = find_x(564)
print(result)
