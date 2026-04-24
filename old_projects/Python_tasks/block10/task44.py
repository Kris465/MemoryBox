def digital_root(n):

    if n < 10:
        return n
    else:

        digit_sum = sum(int(digit) for digit in str(n))

        return digital_root(digit_sum)


number = 38
print(f"Цифровой корень числа {number}: {digital_root(number)}")
