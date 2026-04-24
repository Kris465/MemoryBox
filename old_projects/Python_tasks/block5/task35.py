def alternating_sum(n):
    s = 0
    sing = 1
    for i in range(1, n + 1):
        s += sing * (1 / i)
        sing *= -1
    return s


n = 10
result = alternating_sum(n)
print(result)
