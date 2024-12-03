#Маклюсов

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
n = int(input("Количество чисел в ряду: "))


def fib(n):
    fib_p = []
    a, b = 0, 1
    for _ in range(n):
        fib_p.append(a)
        a, b = b, a + b
    return fib_p


print(fib(n))

