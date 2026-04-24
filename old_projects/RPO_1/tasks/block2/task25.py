n = int(input("Введите число n (от 10 до 999, при этом десятки не равны нулю): "))
if n < 10 or n > 999:
    print("Число вне диапазона 10 ≤ n ≤ 999.")
    exit()
found = False
for c in range(1, 10):
    for a in range(1, 10):
        for b in range(0, 10):
            if 100 * c + 10 * a + b == n:
                x = 100 * a + 10 * b + c
                print(f"Для n = {n} найдено число x = {x}")
                found = True
                break
        if found:
            break
    if found:
        break
if not found:
    print(f"Для числа n = {n} подходящее число x не найдено.")
    