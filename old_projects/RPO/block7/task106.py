def is_count_divisible_by_three(m, d):
    total_count = 0
    for divisor in d:
        count = m // divisor
        total_count += count
    return total_count % 3 == 0


m = int(input("Введите натуральное число m: "))
d = list(map(int, input("Введите целые числа d (через пробел): ").split()))

if is_count_divisible_by_three(m, d):
    print("Количество положительных чисел кратно трем.")
else:
    print("Количество положительных чисел не кратно трем.")
