def procedure3(n):
    if n > 0:
        print(n)
        procedure3(n - 1)
        print(n)


procedure3(5)
