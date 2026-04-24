from itertools import product


def a(X, Y, Z):
    return not (Y or (not X and Z)) or Z


def b(X, Y, Z):
    return (X and not (not Y or Z)) or Y


def v(X, Y, Z):
    return not (X or (Y and Z)) or not X


for X, Y, Z in product([False, True], repeat=3):
    print(
        f'X={X} Y={Y} Z={Z} | '
        f'a={a(X, Y, Z)} | '
        f'b={b(X, Y, Z)} | '
        f'в={v(X, Y, Z)}'
    )
