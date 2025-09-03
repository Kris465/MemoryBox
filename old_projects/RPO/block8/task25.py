def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


for number in range(120, 141):
    divisors_count = count_divisors(number)
    print(f"{number}: {divisors_count}")
