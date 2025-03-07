num = input("Введите натуральное число с разными цифрами: ")

max_digit = -1
min_digit = 10
max_pos_from_end = 0
min_pos_from_end = 0

for i, digit in enumerate(reversed(num), start=1):
    digit = int(digit)
    if digit > max_digit:
        max_digit = digit
        max_pos_from_end = i
    if digit < min_digit:
        min_digit = digit
        min_pos_from_end = i

max_pos_from_start = len(num) - max_pos_from_end + 1
min_pos_from_start = len(num) - min_pos_from_end + 1

print(f"Порядковый номер максимальной цифры от конца: {max_pos_from_end}")
print(f"Порядковый номер максимальной цифры от начала: {max_pos_from_start}")
print(F"Порядковый номер минимальный цифры от конца: {min_pos_from_end}")
print(f"Порядковый номер минимальной цифры от начала: {min_pos_from_start}")
