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


n = 10
print(f"{n}-е число Фибоначчи: {fibonacci(n)}")
