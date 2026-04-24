num = [
 (True, True, True), (True, False, True), (False, True, True),
 (True, True, False), (False, False, False), (False, True, False),
 (True, False, False), (False, False, True)]


def compute_expressions(X, Y, Z):
    a = not (X or not Y and Z)
    b = Y or (X and not Y or Z)
    c = not (not X and Y or Z)
    return a, b, c


for A, B, C in num:
    print(compute_expressions(A, B, C))
