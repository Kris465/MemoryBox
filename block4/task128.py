def how_old_are_you(n):
    year = n // 360
    month = n % 100
    if year == 0:
        if month == 1:
            result = f"{month} копейка"
        elif 2 <= month <= 4:
            result = f"{month} копейки"
        else:
            result = f"{month} копеек"
    else:
        if year == 1:
            ruble_word = "рубль"
        elif 2 <= year <= 4:
            ruble_word = "рубля"
        else:
            ruble_word = "рублей"

        if month == 1:
            copy_word = "копейка"
        elif 2 <= month <= 4:
            copy_word = "копейки"
        else:
            copy_word = "копеек"

        result = f"{year} {ruble_word} {month} {copy_word}"
    return result


a = int(input('Введите число (1 < n < 1188): '))
