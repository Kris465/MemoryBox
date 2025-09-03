def is_palindrome(n):
    """ Функция проверяет, является ли число n палиндромом. :param n: \
        натуральное число :return: True, если число палиндром, иначе False """
    return str(n) == str(n)[::-1]


number1 = int(input("Введите первое натуральное число: "))
number2 = int(input("Введите второе натуральное число: "))

if is_palindrome(number1) or is_palindrome(number2):
    print("Хоть одно из чисел является палиндромом.")
else:
    print("Ни одно из чисел не является палиндромом.")
