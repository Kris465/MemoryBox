def min_bills_for_amount(amount, denominations):
    result = {}
    for denom in sorted(denominations, reverse=True):
        count = amount // denom
        if count > 0:
            result[denom] = count
            amount -= count * denom
    return result


denominations = [1, 2, 4, 8, 16, 32, 64]

n = int(input("Введите сумму n: "))


for i in range(n, n + 11):
    bills = min_bills_for_amount(i, denominations)
    print(f"Минимальное количество купюр для {i}: {bills}")
