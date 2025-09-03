def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_gcd_of_list(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = gcd(result, number)
    return result


numbers = list(map(int, input(
    "Введите натуральные числа через пробел: ").strip().split()))
gcd_value = find_gcd_of_list(numbers)
print("Наибольший общий делитель:", gcd_value)
