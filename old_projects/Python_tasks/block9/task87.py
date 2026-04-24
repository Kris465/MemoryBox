import re


def fix_cha_sha(text):
    text = re.sub(r'чя', 'ча', text)
    text = re.sub(r'шя', 'ша', text)

    return text


input_text = input("Введите последовательность слов: ")
corrected_text = fix_cha_sha(input_text)
print(f"Исправленная строка:\n{corrected_text}")
