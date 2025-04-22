def sum_and_max_digits(text):
    digits = [int(char) for char in text if char.isdigit()]
    total_sum = sum(digits)
    max_digit = max(digits) if digits else None
    return total_sum, max_digit


text = "В этом тексте 1, 2, 3 и 4, а также 5 и 6."
total_sum, max_digit = sum_and_max_digits(text)
print("Сумма цифр:", total_sum)
print("Максимальная цифра:", max_digit)
