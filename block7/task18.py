def find_sum(n):

    return n * (n + 1)


n = int(input("Введите количество элементов: "))


result = find_sum(n)
print(f"Сумма первых {n} элементов последовательности: {result}")
