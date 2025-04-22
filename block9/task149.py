import re

text = input("Введите текст: ")


def extract_number_from_text(text):
    digits = re.findall(r'\d+', text)
    number = ''.join(digits)
    return int(number) if number else None


result = extract_number_from_text(text)
print(result)
