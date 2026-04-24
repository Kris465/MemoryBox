def find_numbers_divisible_by_13():
    result = []
    for number in range(10, 100):
        tens = number // 10
        units = number % 10
        squares_sum = tens**2 + units**2
        if squares_sum % 13 == 0:
            result.append(number)
    return result


def find_special_numbers():
    result = []
    for number in range(10, 100):
        tens = number // 10
        units = number % 10
        digits_sum = tens + units
        if number == digits_sum + digits_sum**2:
            result.append(number)
    return result


divisible_numbers = find_numbers_divisible_by_13()
print("Все двузначные числа, сумма квадратов цифр которых делится на 13:")
print(divisible_numbers)


special_numbers = find_special_numbers()
print("\nВсе двузначные числа, обладающие указанным свойством:")
print(special_numbers)
