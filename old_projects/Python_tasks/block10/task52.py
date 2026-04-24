def reverse_print(n):
    if n < 10:
        print(n, end=" ")
    else:
        print(n % 10, end=" ")
        reverse_print(n // 10)


reverse_print(12345)
