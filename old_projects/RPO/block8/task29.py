def count_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i:
                divisors += 1
            else:
                divisors += 2
    return divisors


def find_numbers_with_k_divisors(a, b, k):
    result = []
    for n in range(a, b + 1):
        if count_divisors(n) == k:
            result.append(n)
    return result


a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
k = int(input("Введите количество делителей: "))

numbers = find_numbers_with_k_divisors(a, b, k)
print(f"Числа с {k} делителями в диапазоне от {a} до {b}: {numbers}")
