def fibonacci_sequence(N):
    if N <= 0:
        return []
    
    sequence = [1]
    a, b = 1, 1

    for _ in range(1, N):
        a, b = b, a + b
        sequence.append(b)
    
    return sequence

# Пример использования функции
N = 10  # количество элементов последовательности
print(fibonacci_sequence(N))
