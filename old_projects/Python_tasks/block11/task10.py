def fill_reversed_digits(n):
    # Преобразуем число в строку и переворачиваем её
    reversed_str = str(n)[::-1]

    # Формируем массив из шести элементов, дополняя нулями
    digits = [int(char) for char in reversed_str] + [0]*(6 - len(reversed_str))

    # Выводим массив
    print("Элементы массива (заполненные цифры и нули):", digits)


n = int(input("Введите натуральное число (до 999999): "))
fill_reversed_digits(n)
