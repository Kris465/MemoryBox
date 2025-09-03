def power(a, n):

    if n == 0:
        return 1

    else:
        return a * power(a, n - 1)


print(power(2, 3))
print(power(5, 0))
print(power(-3, 4))
