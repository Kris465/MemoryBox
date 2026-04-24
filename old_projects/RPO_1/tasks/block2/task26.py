for b in range(10):
    for c in range(10):
        a = 564 - 100*b - 10*c
        if 1 <= a <= 9:
            x = 100*a + 10*b + c
            print(f"Найдено число x = {x}")
