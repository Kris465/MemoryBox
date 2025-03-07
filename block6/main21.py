def fibonacci(limit):
    fib = [0, 1]
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib < limit:
            fib.append(next_fib)
        else:
            break
    return fib

# Пример использования
print(fibonacci(1000))
