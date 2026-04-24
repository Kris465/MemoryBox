def sum_proper_divisors(n):
    if n == 1:
        return 0
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum


divisor_sums = {}


friendly_pairs = []
for num in range(1, 50000):

    divisor_sums[num] = sum_proper_divisors(num)
    pair = divisor_sums[num]

    if pair > num and pair in divisor_sums and divisor_sums[pair] == num:
        friendly_pairs.append((num, pair))

print("Дружественные пары чисел:", friendly_pairs)
