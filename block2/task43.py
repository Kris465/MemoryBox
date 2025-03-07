def check_divisibility(a, b):

    result = (a % b == 0) or (b % a == 0)

    return 1 if result else 0


a = 10
b = 2
output = check_divisibility(a, b)
print(output)