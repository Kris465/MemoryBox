def sum_of_divisors(num):
    total = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            total += i
    return total


def is_perfect_number(N):
    if N < 1:
        return False
    return sum_of_divisors(N) == N


# Пример использования
N = int(input("Введите натуральное число N: "))
print(f"{N} является совершенным числом: {is_perfect_number(N)}")