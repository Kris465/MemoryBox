d = list(map(int, input("Введите десять целых чисел через пробел: ").split()))


sum_even = 0


for number in d:
    if number % 2 == 0:
        sum_even += number

print(f"Сумма четных чисел: {sum_even}")
