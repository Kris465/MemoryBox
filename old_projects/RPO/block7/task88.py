def is_sum_even(numbers):
    return sum(numbers) % 2 == 0


numbers = [1, 2, 3, 4]
result = is_sum_even(numbers)
print(f"Сумма четная: {result}")
