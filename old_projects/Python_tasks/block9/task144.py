def sum_of_digits(text):
    return sum(int(char) for char in text if char.isdigit())


text = "12345"
result = sum_of_digits(text)
print("Сумма цифр:", result)
