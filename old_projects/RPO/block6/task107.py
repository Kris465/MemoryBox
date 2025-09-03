# 1 способ
m = 3
n = 4
result = list(range(m, m * n + 1, m))
print(result)

# 2 способ
m = 3
n = 4
result = [i for i in range(m, m * n + 1) if i % m == 0]
print(result)
