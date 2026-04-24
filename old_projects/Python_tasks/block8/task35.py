def sum_of_divisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total


result = []
for number in range(300, 601):
    if sum_of_divisors(number) % 10 == 0:
        result.append(number)

print("Числа от 300 до 600, у которых сумма делителей кратна 10:")
print(result)
