def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]


# Ввод данных
n = int(input("Введите количество чисел Фибоначчи: "))


# Заполнение массива
result = fibonacci(n)
print("Числа Фибоначчи:", result)
