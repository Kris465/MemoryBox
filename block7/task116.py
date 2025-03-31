m = int(input("Введите количество чисел m: "))
n = int(input("Введите число n: "))

a = list(map(int, input("Введите последовательность целых чисел через пробел: ").split()))

multiples_of_n = [i for i in a if i % n == 0]

if multiples_of_n:
    average = sum(multiples_of_n) / len(multiples_of_n)
    print(f"Среднее арифметическое чисел, кратных {n}: {average:.2f}")
else:
    print(f"Нет чисел, кратных {n}.")
