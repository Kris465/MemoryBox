num = [(True, True), (True, False), (False, True), (False, False)]


def compute_expressions(a, b):
    x = (not a and not b) or a
    y = b or (not a and not b)
    z = b and not (a and not b)
    return x, y, z


for a, b in num:
    x, y, z = compute_expressions(a, b)
    print(f"a = {a}, b = {b}:")
    print(f"\ta) not a and not b or a = {x}")
    print(f"tb) b or not a and not b = {y}")
    print(f"\tv) b and not (a and not b) = {z}")
    print()
