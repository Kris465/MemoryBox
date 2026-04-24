def is_palindrome(s):
    s = s.replace(" ", "").rstrip("_")
    return s == s[::-1]


string = input("Введите строку: ")
if is_palindrome(string):
    print("Строка является перевертышем.")
else:
    print("Строка не является перевертышем.")
