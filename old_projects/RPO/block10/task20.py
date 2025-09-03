def sum_of_three_digits(n):
    """Возвращает сумму цифр трехзначного числа n."""
    s = str(n)
    return int(s[0]) + int(s[1]) + int(s[2])


happy_numbers = []


for number in range(100000, 1000000):
    first_part = number // 1000
    second_part = number % 1000

    if sum_of_three_digits(first_part) == sum_of_three_digits(second_part):
        happy_numbers.append(number)


for num in happy_numbers:
    print(num)
