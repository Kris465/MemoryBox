num = [
    (True, True, True), (True, False, True), (False, True, True),
    (True, True, False), (False, False, False), (False, True, False),
    (True, False, False), (False, False, True)]


def compute_expressions(X, Y, Z):
    a = not (Y or not X and Z) or Z
    b = X and not (not Y or Z) or Y
    c = not (X or Y and Z) or not X
    return a, b, c


for A, B, C in num:
    print(compute_expressions(A, B, C))
