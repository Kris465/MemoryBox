
expression_a = "-1 / x**2"

expression_b = "(a + b) / 2"


expression_c = "(-b + 1/a) / 2"


expression_d = "2**(n'')"


expression_6 = "a / (b * c)"


expression_7 = "5.45 * (a + 2*b) / (2 - a)"


expression_8 = "3 / (1 + (a + b) / 2)"


expression_9 = "a / b"


expression_10 = "(-b + (b**2 - 4*a*c)**0.5) / (2*a)"


expression_11 = "1 / (1 + 1/2 + 1 / (2 + 3/5))"


expressions = [expression_a, expression_b, expression_c, expression_d,
               expression_6, expression_7, expression_8, expression_9,
               expression_10, expression_11
               ]

for i, expr in enumerate(expressions, start=1):
    print(f"Expression {i}: {expr}")
