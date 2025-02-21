def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def sum_factorials(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total


n = int(input("Введите число n (1 < n < 10): "))
print(sum_factorials(n))
