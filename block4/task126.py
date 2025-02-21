def find_mahrooms(k):
    if 11 <= k % 100 <= 14:
        suffix = 'грибов'
    else:
        last_digit = k % 10
        if last_digit == 1:
            suffix = "гриб"
        elif 2 <= last_digit <= 4:
            suffix = "грибa"
        else:
            suffix = "грибов"
    return f"мы нашли {k} {suffix} в лесу"

    k = int(input("введите количество грибов: "))
    print(find_mahrooms(k))
