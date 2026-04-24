def minutes_until_clock_hands_meet(h, m):
    # Обратное число к 11 по модулю 720
    inverse_11 = 131

    # Вычисляем r
    r = (60 * h - 11 * m) % 720

    # Находим минимальное t
    t = (inverse_11 * r) % 720

    # Если t=0, то следующий совпадение через 12 часов
    if t == 0:
        t = 720
    return t

# Пример использования:
    h = int(input("Введите часы (1-12): "))
    m = int(input("Введите минуты (0-59): "))

    result = minutes_until_clock_hands_meet(h, m)
    print(f"Наименьшее полное число минут до следующего совпадения: {result}")
