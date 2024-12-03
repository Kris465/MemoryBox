n = int(input("Введите размер массива: "))


def fibonacci(n):
    fib = [0, 1]
    for x in range(2, n):
        fib.append(fib[-2] + fib[-1])

    return fib[:n]


result = fibonacci(n)
print("Числа Фибоначчи:", result)
