n = int(input("Введите количество вещественных чисел: "))
numbers = list(map(float, input("Введите вещественные числа через пробел: ").split()))
p = float(input("Введите значение p: "))

sum_numbers = sum(x for x in numbers if x > 20.5)

if sum_numbers < p:
    print("Сумма чисел больше 20.5 меньше p.")
else:
    print("Сумма чисел больше 20.5 не меньше p.")
