n = int(input("Введите натуральное число n: "))
numbers = []


for i in range(n):
    num = int(input(f"Введите число d{i + 1}: "))
    numbers.append(num)


m = int(input("Введите число m: "))
p = int(input("Введите число p: "))


sum_less_than_or_equal_m = sum(num for num in numbers if num <= m)


is_sum_multiple_of_p = sum_less_than_or_equal_m % p == 0


print(f"Сумма чисел, не превышающих {m}, кратна {p}: {is_sum_multiple_of_p}")
