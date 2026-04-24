combinations = [
    (A, B, C)
    for A in [0, 1]
    for B in [0, 1]
    for C in [0, 1]
]

print("A B C | (а) | (б) | (в)")
print("-------------------------")

for A, B, C in combinations:
    expr_a = (not (A or (not B) and C)) or C
    expr_b = (not ((A and (not B)) or C)) and B
    expr_v = (not ((not A) or (B and C))) or A
    print(f"{A} {B} {C} |  {int(expr_a)}  |  {int(expr_b)}  |  {int(expr_v)}")
