def integer_division(a, b):
    count = 0
    while a >= b:
        a -= b
        count += 1
    return count, a


a = 17
b = 5
quotient, reminder = integer_division(a, b)
print(f"Цулочисленное деление{a} на {b} равно {quotient},\
    остаток равен {reminder}")
