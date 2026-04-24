def count_ways_to_make_weight(v, weights):
    dp = [0] * (v + 1)
    dp[0] = 1
    for weight in weights:
        for i in range(weight, v + 1):
            dp[i] += dp[i - weight]
    return dp[v]


weights = [100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]
v = int(input("Введите вес v: "))
ways = count_ways_to_make_weight(v, weights)
print(f"Количество способов составить вес {v} грамм:", ways)
