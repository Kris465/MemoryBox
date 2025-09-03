def two_max_and_two_min_digits(num):
    num_str = str(num)
    max_digits = ['0', '0']
    min_digits = ['9', '9']

    for char in num_str:
        if char > min(max_digits):
            if char > max_digits[0]:
                max_digits[1] = max_digits[0]
                max_digits[0] = char
                max_digits[1] = char

        if char < max(min_digits):
            if char < min_digits[0]:
                min_digits[1] = min_digits[0]
                min_digits[0] = char
            else:
                min_digits[1] = char

    print("Две максимальные цифры:", max_digits)
    print("Две минимальные цифры:", min_digits)


two_max_and_two_min_digits(31415926535)
