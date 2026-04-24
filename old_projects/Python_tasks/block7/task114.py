x = int(input("Введите натуральное число x: "))
n = int(input("Введите число n: "))
a = list(map(int, input("Введите числа a1, a2, ..., ax через пробел:\
    ").split()))

filtered_a = [ai for ai in a if ai > n]

if filtered_a:
    average = sum(filtered_a) / len(filtered_a)
    print(f"Среднее арифметическое чисел, больших {n}: {average:.2f}")
else:
    print(f"Нет чисел, больших {n}.")
