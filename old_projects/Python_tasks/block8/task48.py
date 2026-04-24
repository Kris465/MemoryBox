def coin_change_ways(n):
    coins = [1, 2, 5, 10]
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]

    return dp[n]


def get_all_coin_combinations(n):
    coins = [1, 2, 5, 10]
    dp = [[[]]] * (n + 1)
    dp[0] = [[]]

    for coin in coins:
        for amount in range(coin, n + 1):
            for prev_solution in dp[amount - coin]:
                new_solution = prev_solution.copy()
                new_solution.append(coin)
                dp[amount].append(new_solution)

    return dp[n]


n = int(input("Введите сумму n: "))
ways = coin_change_ways(n)
print(f"Количество способов выплаты суммы {n} рублей: {ways}")


all_combinations = get_all_coin_combinations(n)
print(f"Все способы выплаты суммы {n} рублей:")
for combination in all_combinations:
    print(combination)
