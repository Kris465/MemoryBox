def fibonacci(n):
    if n <= 0:
        return "Введите положительное целое число"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_hyperprime(N):
    # Проверяем, является ли N простым и находится ли оно в последовательности Фибоначчи
    if not is_prime(N):
        return False

    # Проверяем, является ли N числом Фибоначчи
    a, b = 0, 1
    while b < N:
        a, b = b, a + b

    return b == N


# Пример использования
N = int(input("Введите натуральное число N для проверки на гиперпростое: "))
print(f"{N} является гиперпростым числом: {is_hyperprime(N)}")
