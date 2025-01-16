def check_four_digit_number(n):
    d1 = n // 1000
    d2 = (n // 100) % 10
    d3 = (n // 10) % 10
    d4 = n % 10

    sum_first_pair = d1 + d2
    sum_last_pair = d3 + d4

    total_sum = d1 + d2 + d3 + d4

    product_digits = d1 * d2 * d3 * d4

    a = 5

    result_a = sum_first_pair == sum_last_pair
    result_b = total_sum % 3 == 0
    result_c = product_digits % 4 == 0
    result_d = product_digits % a == 0

    return {
        "a": result_a,
        "b": result_b,
        "c": result_c,
        "d": result_d
    }


number = 1234
results = check_four_digit_number(number)
print(results)
