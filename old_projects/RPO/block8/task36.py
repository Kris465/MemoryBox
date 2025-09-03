def sum_of_divisors(n):
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total


perfect_numbers = []
for number in range(2, 100000):
    if sum_of_divisors(number) == number:
        perfect_numbers.append(number)

print(perfect_numbers)
