def is_sum_multiple(numbers, b):
    return sum(numbers) % b == 0


numbers = [10, 20, 30]
b = 10
result = is_sum_multiple(numbers, b)
print(f"Сумма чисел кратна {b}: {result}")
