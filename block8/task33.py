def sum_of_divisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total


for number in range(50, 71):
    divisors_sum = sum_of_divisors(number)
    print(f"{number}: {divisors_sum}")
