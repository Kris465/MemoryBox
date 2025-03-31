def count_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i:
                divisors += 1
            else:
                divisors += 2
    return divisors


def find_max_min_divisors(a, b):
    max_number = None
    min_number = None
    max_divisors = 0
    for n in range(a, b + 1):
        divisors = count_divisors(n)
        if divisors > max_divisors:
            max_divisors = divisors
            max_number = n
            min_number = n
        elif divisors == max_divisors:
            if n < min_number:
                min_number = n
            if n > max_number:
                max_number = n
    return max_number, min_number


a = int(input())
b = int(input())
max_num, min_num = find_max_min_divisors(a, b)
print(max_num)
print(min_num)
