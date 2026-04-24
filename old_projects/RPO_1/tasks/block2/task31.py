n = int(input("Введите число n (от 100 до 999): "))

x_found = None

for A in range(1, 10):       
    for B in range(0, 10):
        for C in range(0, 10):
            
            if (10 * A + C) * 10 + B == n:
                x = 100 * A + 10 * B + C
                print(f"Исходное число x = {x}")
                x_found = x
                break
        if x_found is not None:
            break
    if x_found is not None:
        break

if x_found is None:
    print("Соответствующее число x не найдено.")