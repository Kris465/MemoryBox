def min_coins(n):
    denominations = [64, 32, 16, 8, 4, 2, 1]  # номиналы купюр в порядке убывания
    coins = {}

    for denom in denominations:
        count = n // denom  # количество купюр данного номинала
        if count > 0:
            coins[denom] = count
            n -= count * denom  # уменьшаем оставшуюся сумму

    return coins

# Пример использования
n = 123
result = min_coins(n)
print(f"Минимальное количество купюр для выплаты суммы {n}:")
for denom, count in result.items():
    print(f"{count} купюр по {denom}")
