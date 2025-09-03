def sum_of_divisors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)


result = [num for num in range(100, 301) if sum_of_divisors(num) == 50]

print("Числа с суммой делителей, равной 50:", result)
