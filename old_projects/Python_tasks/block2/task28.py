for x in range(100, 1000):
    str_x = str(x)
    second_digit = str_x[1]
    new_number = int(second_digit + str_x[0] + str_x[2])
    if new_number == 546:
        print(f"Найдено число x: {x}")
        break
