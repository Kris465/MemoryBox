def reverse_number(n):
    reversed_str = str(n)[::-1]
    return int(reversed_str)


def append_twos(n):
    twos_appended = '22' + str(n) + '22'
    return int(twos_appended)


def remove_digit_a(n, digit='a'):
    digits_removed = str(n).replace(digit, '')
    if not digits_removed:
        return None
    return int(digits_removed)


def swap_first_last_digits(n):
    num_str = str(n)
    first_digit = num_str[0]
    last_digit = num_str[-1]

    if len(num_str) == 1:
        return n

    swapped_num = last_digit + num_str[1:-1] + first_digit
    return int(swapped_num)


def double_the_number(n):
    doubled = str(n) + str(n)
    return int(doubled)


number = int(input('Введите любое натуральное число: '))

reversed_num = reverse_number(number)
print("Число, прочитанное справа налево:", reversed_num)

twos_appended_num = append_twos(number)
print("Число с приписанными двойками:", twos_appended_num)

removed_digit_a_num = remove_digit_a(number, '5')
print("Число без цифры '5':", removed_digit_a_num)

swapped_num = swap_first_last_digits(number)
print("Число с переставленными первой и последней цифрами:", swapped_num)

doubled_num = double_the_number(number)
print("Удвоенное число:", doubled_num)
