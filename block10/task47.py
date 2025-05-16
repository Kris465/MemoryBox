def fibonacci(k):

    if k <= 2:
        return 1
    else:

        return fibonacci(k - 1) + fibonacci(k - 2)


position = 10
fib_value = fibonacci(position)
print(f"{position}-й член последовательности Фибоначчи: {fib_value}")
