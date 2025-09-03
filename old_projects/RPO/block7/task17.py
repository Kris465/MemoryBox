def sum_of_multipes(m, n, numbers):
    return sum(x for x in numbers if x % n == 0)


m = int(input("Введите количество чисел: "))
n = int(input("Введите число: "))
numbers = [int(input(f"Введите число {i + 1}:")) for i in range(m)]

result = sum_of_multipes(m, n, numbers)
print(f"Сумма чисел кратных {n} : {result}")
