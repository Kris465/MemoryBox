def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]

number = int(input("Введите натуральное число: "))

if is_palindrome(number):
    print(f"{number} является палиндромом.")
else:
    print(f"{number} не является палиндромом.")
