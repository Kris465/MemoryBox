a = [1, 2, 3, 4, 5, 6]

sum_alternating = 0

sign = 1

for element in a:
    sum_alternating += sign * element
    sign *= -1

print("Знакопеременная сумма:", sum_alternating)