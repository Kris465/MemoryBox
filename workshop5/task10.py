# Создайте функцию генератор чисел Фибоначчи (см. Википедию)


def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


print(list(fib(22)))
