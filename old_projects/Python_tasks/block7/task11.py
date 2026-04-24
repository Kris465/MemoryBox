three_digit_numbers = []
for i in range(100, 1000):
    if str(i**2).endswith(str(i)):
        three_digit_numbers.append(i)
print(three_digit_numbers)


seven_multiple_numbers = []
for i in range(100, 1000):
    if i % 7 == 0 and sum(int(digit) for digit in str(i)) % 7 == 0:
        seven_multiple_numbers.append(i)
print(seven_multiple_numbers)
