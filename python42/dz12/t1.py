def is_palindrome():
    user_input = input("Введите строку: ")
    cleaned_input = ''.join(user_input.split()).lower()

    if cleaned_input == cleaned_input[::-1]:
        print("Введенная строка является палиндромом.")
    else:
        print("Введенная строка не является палиндромом.")


is_palindrome()
