def check_conditions(bs):
    sum_above_20 = sum(x for x in bs if x > 20)
    condition_a = sum_above_20 > 100

    sum_below_50 = sum(x for x in bs if x < 50)
    condition_b = sum_below_50 % 2 == 0

    return condition_a, condition_b


bs = [23, 51, 19, 71, 29, 41, 83, 37, 59, 47]
condition_a, condition_b = check_conditions(bs)

print("Сумма чисел, больших 20, превышает 100:", condition_a)
print("Сумма чисел, меньших 50, является четным числом:", condition_b)
