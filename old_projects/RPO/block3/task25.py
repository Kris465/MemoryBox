num = [(True, True, True), (True, False, True), (False, True, True),
       (True, True, False), (False, False, False), (False, True, False),
       (True, False, False), (False, False, True)]


def compute_expression(A, B, C):
    a = not (A and B) and (not A or not C)
    b = not (A or not B) or (A or not C)
    c = A or not B or not (A or not C)
    return a, b, c


for A, B, C in num:
    print(compute_expression(A, B, C))
