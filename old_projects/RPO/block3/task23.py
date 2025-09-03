def calculate_and_print(a, b, c):
    expr_a = not (a or (not b and c)) or c
    expr_b = not (a and (not b or c)) and b
    expr_c = not ((not a) or (b and c))
    print(f'a = {a}, b = {b}, c = {c}')
    print(f'a) {expr_a}')
    print(f'b) {expr_b}')
    print(f'c) {expr_c}')
    print()


for a in [False, True]:
    for b in [False, True]:
        for c in [False, True]:
            calculate_and_print(a, b, c)
