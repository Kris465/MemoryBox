def process_number(n):
    number_str = str(n)
    digit_count = len(number_str)
    sum_of_digits = sum(int(digit) for digit in number_str)
    product_of_digits = 1
    for digit in number_str:
        product_of_digits *= int(digit)
    average_of_digits = sum_of_digits / digit_count
    sum_of_squares = sum(int(digit)**2 for digit in number_str)
    sum_of_cubes = sum(int(digit)**3 for digit in number_str)
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
    sum_first_last = first_digit + last_digit

    return {
        'a': digit_count,
        'b': sum_of_digits,
        'c': product_of_digits,
        'd': average_of_digits,
        'e': sum_of_squares,
        'f': sum_of_cubes,
        'g': first_digit,
        'h': last_digit,
        'z': sum_first_last
    }


number = 12345
results = process_number(number)
for key, value in results.items():
    print(f"{key}) {value}")
