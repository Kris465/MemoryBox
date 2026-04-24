n = int(input("Введите число n (от 1 до 999), где последняя цифра != 0: "))

# Проверяем, что последняя цифра n не равна 0
if n % 10 == 0:
    print("Последняя цифра числа n должна быть не равна нулю.")
else:
    x_found = None
    
    for C in range(1, 10):  # C не может быть 0, так как число трехзначное
        for B in range(0, 10):
            for A in range(1, 10):  # A не может быть 0
                if 100 * C + 10 * B + A == n:
                    # Нашли подходящую комбинацию
                    x = 100 * A + 10 * B + C
                    print(f"Значение x = {x}")
                    x_found = x
                    break
            if x_found is not None:
                break
        if x_found is not None:
            break

    if x_found is None:
        print("Подходящее число x не найдено.")
