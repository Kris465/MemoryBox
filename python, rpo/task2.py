def is_palindrome(input_string):
    # Убираем пробелы и специальные символы, приводим к нижнему регистру
    cleaned_string = ''.join(
        char.lower() for char in input_string if char.isalnum())

    # Сравниваем очищенную строку с её реверсией
    return cleaned_string == cleaned_string[::-1]


# Примеры использования
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("Was it a car or a cat I saw?"))    # True
print(is_palindrome("Hello, World!"))                    # False
