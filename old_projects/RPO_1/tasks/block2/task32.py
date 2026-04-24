for C in range(1, 10):
    for B in range(0, 10):
        for A in range(0, 10):
            if 100 * C + 10 * B + A == 654:
                # Нашли цифры исходного числа
                x = 100 * A + 10 * B + C
                print(f"Исходное число x = {x}")
                break
        else:
            continue
        break
    else:
        continue
    break
else:
    print("Число не найдено.")
    