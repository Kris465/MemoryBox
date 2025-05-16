def factorial(n):
    # Базовый случай: если n равно 0 или 1, возвращаем 1
    if n == 0 or n == 1:
        return 1
    else:
        # Рекурсивный случай: умножаем n на факториал (n-1)
        return n * factorial(n - 1)


for i in range(6):  # Факториалы чисел от 0 до 5
    print(f"{i}! = {factorial(i)}")
