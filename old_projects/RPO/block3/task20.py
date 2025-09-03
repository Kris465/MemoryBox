num = [{True, True}, {True, False}, {False, True}, {False, False}]


def compute_expressions(X, Y):
    a = not (not X or Y) or not X
    b = not (not X and not Y) and X
    c = not (X or not Y) or not Y
    return a, b, c


for X, Y in num:
    a, b, c = compute_expressions(X, Y)
    print(f"Х = {X}, Y = {Y}")
    print(f"а) не (не X или Y) или не Х = {a}")
    print(f"б) не (не Х и не Y) и Х = {b}")
    print(f"с) не (Х или не Y) или не Y = {c}")
