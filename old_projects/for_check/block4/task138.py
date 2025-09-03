def find_digit(n):

    sequence = 1234567891011121314151617181920

    digit = (sequence // (10**(31-n))) % 10

    return digit


n = int(input("введите номер цифры (от 1 до 32): "))
result = find_digit(n)
print(f"цифры под номером {n}: {result}")
