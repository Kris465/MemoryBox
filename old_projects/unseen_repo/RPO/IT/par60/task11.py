def digit_sum(n):
    """Функция для вычисления суммы цифр числа n."""
    return sum(int(digit) for digit in str(n))


def find_special_numbers(N):
    """Функция для нахождения чисел, сумма цифр которых не меняется при умножении на 2-9."""
    special_numbers = []
    for i in range(N + 1):
        original_sum = digit_sum(i)
        if all(original_sum == digit_sum(i * multiplier) for multiplier in range(2, 10)):
            special_numbers.append(i)
    return special_numbers


# Получаем число N от пользователя
N = int(input("Введите число N: "))
special_numbers = find_special_numbers(N)

print("Числа с неизменной суммой цифр:", special_numbers)
