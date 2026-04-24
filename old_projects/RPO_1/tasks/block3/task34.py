a, b, c, d = map(int, input().split())

# а) ладья
condition_a = (a == c or b == d)

# б) слон
condition_b = abs(a - c) == abs(b - d)

# в) король
condition_v = abs(a - c) <= 1 and abs(b - d) <= 1

# г) ферзь
condition_g = (a == c or b == d) or (abs(a - c) == abs(b - d))

# д) белая пешка
condition_d = (
    (a == c and b + 1 == d) or
    (abs(a - c) == 1 and b + 1 == d)
)