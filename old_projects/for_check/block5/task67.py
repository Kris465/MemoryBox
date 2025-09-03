def fibonacci_kth_term(n, k):
    if n <= 2:
        return 1

    previous = 1
    current = 1
    count = 2

    while count < n:
        next_value = previous + current
        previous = current
        current = next_value
        count += 1

    return current


n = 8
k = 5
result = fibonacci_kth_term(n, k)
print("k-й член последовательности Фибоначчи при n={} и k={}: [result]")
