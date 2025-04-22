text = "Пример текста с цифрами 12345 и 678."
cleaned_text = "".join(c if c.isdigit() else " " for c in text)
max_count = max(len(s) for s in cleaned_text.split())
print("Максимальное количество цифр подряд:", max_count)
