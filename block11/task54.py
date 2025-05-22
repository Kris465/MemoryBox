arr = list(map(float, input("Введите массив чисел через пробел: ").split()))

a = float(input("Введите число a: "))

sum_not_exceed_20 = sum(x for x in arr if x <= 20)

sum_greater_a = sum(x for x in arr if x > a)

print("Сумма элементов, не превышающих 20:", sum_not_exceed_20)
print("Сумма элементов, больших числа a:", sum_greater_a)
