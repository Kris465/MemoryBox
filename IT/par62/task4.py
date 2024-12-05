from random import randint

n = int(input("Введите количество элементов: "))
a = [randint(0, 100) for i in range(1, n+1)]

print(f'Ваш начальное количество элементов было: {n}, вот список: {a}')
