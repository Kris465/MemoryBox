k = int(input("Введите число: "))
if k >= 1 and k <= 100:
    if k % 2 == 0:
        print(k // 2 - 1)
    elif k % 2 > 0:
        print(k // 20 + 1)
