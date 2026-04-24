n = int(input("Введите число n (1 ≤ n ≤ 999): "))

if not (1 <= n <= 999):
    print("Число n вне допустимого диапазона.")
    exit()

found = False
for a in range(1, 10):       # первая цифра x
    for b in range(10):      # вторая цифра x
        for c in range(10):  # третья цифра x
            if n == 100*b + 10*c + a:
                x = 100*a + 10*b + c
                print(f"Для n = {n} число x = {x}")
                found = True
                break
        if found:
            break
    if found:
        break

if not found:
    print("Число x не найдено.")
