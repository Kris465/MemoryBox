n = int(input("Введите число (1 <= n <= 999): "))
for last_digit in range(1, 10):
    two_digit_number = n % 100
    if two_digit_number // 10 != last_digit:
        first_digit = two_digit_number % 10
        x = last_digit * 100 + first_digit * 10 + last_digit
        if x < 1000:
            print(x)
