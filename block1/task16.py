expression_a = "a / b / c"

expression_b = "a - b / c"

expression_c = "a + b / c"

expression_d = "(a + b) / (b + c)"

expression_e = "a + b / (b + c)"

expression_f = "(a + b) / b + c"

expression_g = "a / 2 * b * c * a * b * x"

expression_h = "2 * b * c * math.cos(a / 2) / (b + c)"

expression_i = "4 * R * math.sin(a / 2) * math.sin(b / 2) * math.sin(c / 2)"

expression_j = "(a * x + b) / (c * x + d)"

expression_k = "2 * math.sin((a + b) / 2) * math.cos((a - b) / 2)"

expression_l = "abs(2 * math.sin(-3 * abs(x / 2)))"

expressions = [
    expression_a, expression_b, expression_c, expression_d,
    expression_e, expression_f, expression_g, expression_h,
    expression_i, expression_j, expression_k, expression_l
    ]
for i, expr in enumerate(expressions, start=1):
    print(f"Expression {chr(96 + i)}: {expr}")
