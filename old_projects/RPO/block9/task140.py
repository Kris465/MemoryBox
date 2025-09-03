text = input("Введите текст с цифрами: ")


def count_digits(text):
    return sum(1 for char in text if char.isdigit())


digit_count = count_digits(text)
print(digit_count)
