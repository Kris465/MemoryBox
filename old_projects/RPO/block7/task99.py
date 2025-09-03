n = int(input("Введите количество целых чисел: "))
numbers = list(map(int, input("Введите целые числа через пробел: ").split()))
m = int(input("Введите значение m: "))
q = int(input("Введите значение q: "))

sum_numbers = sum(a for a in numbers if a <= m)

if sum_numbers > q:
    print("Сумма чисел, которые не больше m, превышает q.")
else:
    print("Сумма чисел, которые не больше m, не превышает q.")
