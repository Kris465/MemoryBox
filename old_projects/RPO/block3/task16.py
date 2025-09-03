num = [(True, True), (True, False), (False, True), (False, True)]


def compute_expressions(X, Y):
    a = not X and not Y
    b = X or (not X and Y)
    c = (not X and Y) or Y
    return a, b, c


for X, Y in num:
    a, b, c = compute_expressions(X, Y)
    print(f"X={X}, Y={Y}:")
    print(f"\ta) не X и не Y = {a}")
    print(f"\tb) X или (не X и Y) = {b}")
    print(f"\tc) (не X и Y) или Y = {c}")
