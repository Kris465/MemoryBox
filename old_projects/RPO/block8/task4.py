def print_pattern_a(n=5, row=0):
    if row >= n:
        return
    print("".join(str(row - i if i % 2 == 0 else i) for i in range(row + 1)))
    print_pattern_a(n, row + 1)


def print_pattern_b(n=5, start=6, row=0):
    if row >= n:
        return
    print(" ".join(str(start - i) for i in range(n - row)))
    print_pattern_b(n, start + 1, row + 1)


def print_pattern_c(n=5, start=30, row=0):
    if row >= n:
        return
    print(" ".join(str(start - row + i) for i in range(row + 1)))
    print_pattern_c(n, start, row + 1)


def print_pattern_d(n=5, start=20, row=0):
    if row >= n:
        return
    print(" ".join(str(start - row + i) for i in range(n - row)))
    print_pattern_d(n, start, row + 1)


print("а)")
print_pattern_a()

print("\nb)")
print_pattern_b()

print("\nc)")
print_pattern_c()

print("\nd)")
print_pattern_d()
