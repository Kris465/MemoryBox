def multiples_of_m_and_n(m, n):
    for i in range(1, m * n + 1):
        if i % m == 0 and i % n == 0:
            yield i

# Пример использования
m = 3
n = 5
result = list(multiples_of_m_and_n(m, n))
print(f"Все кратные числа для m={m} и n={n}: {result}")
