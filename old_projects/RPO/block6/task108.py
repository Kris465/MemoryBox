def calculate_banknotes(n):
    denominations = [64, 32, 16, 8, 4, 2, 1]
    count = {denom: 0 for denom in denominations}

    for denom in denominations:
        if n >= denom:
            count[denom] = n // denom
            n -= count[denom] * denom

    return count


n = 73
result = calculate_banknotes(n)
print(result)
