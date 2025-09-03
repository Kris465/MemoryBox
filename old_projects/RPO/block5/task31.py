def sum_of_squares(n):
    total_sum = 0
    for i in range(n, 2 * n + 1):
        total_sum += i ** 2
    return total_sum

n = int(input("Введите значение n: "))
result = sum_of_squares(n)
print(f"Сумма квадратов от {n}^2 до (2*{n})^2 равна {result}")
