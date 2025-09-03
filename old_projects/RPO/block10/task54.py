def decimal_to_binary(n):
    if n < 2:
        print(n, end='')
    else:
        decimal_to_binary(n // 2)
        print(n % 2, end='')


decimal_to_binary(13)
print()
