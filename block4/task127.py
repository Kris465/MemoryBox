def convert_to_rubles_and_copies(n):
    rubles = n // 100
    copies = n % 100
    if rubles == 0:
        if copies == 1:
            result = f"{copies} копейка"
        elif 2 <= copies <= 4:
            result = f"{copies} копейки"
        else:
            result = f"{copies} копеек"
    else:
        if rubles == 1:
            ruble_word = "рубль"
        elif 2 <= rubles <= 4:
            ruble_word = "рубля"
        else:
            ruble_word = "рублей"

        if copies == 1:
            copy_word = "копейка"
        elif 2 <= copies <= 4:
            copy_word = "копейки"
        else:
            copy_word = "копеек"

        result = f"{rubles} {ruble_word} {copies} {copy_word}"
    return result


n = int(input("Введите стоимость в копейках: "))
result = convert_to_rubles_and_copies(n)
print(result)
