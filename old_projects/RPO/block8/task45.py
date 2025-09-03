def has_no_duplicate_digits(n):
    digits = str(n)
    return len(digits) == len(set(digits))


three_digit_numbers = [i for i in
                       range(100, 1000) if has_no_duplicate_digits(i)]

for number in three_digit_numbers:
    print(number)
