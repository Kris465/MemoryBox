def is_non_decreasing(num):
    # Преобразуем число в строку и переворачиваем его
    reversed_digits = str(num)[::-1]

    # Проверяем, упорядочены ли цифры
    for i in range(len(reversed_digits) - 1):
        if reversed_digits[i] > reversed_digits[i + 1]:
            return False
    return True


# Примеры использования
number = 5321
if is_non_decreasing(number):
    print(f"Цифры числа {number} справа налево упорядочены по неубыванию.")
else:
    print(f"Цифры числа {number} справа налево не упорядочены по неубыванию.")

number = 9663
if is_non_decreasing(number):
    print(f"Цифры числа {number} справа налево упорядочены по неубыванию.")
else:
    print(f"Цифры числа {number} справа налево не упорядочены по неубыванию.")

number = 7820
if is_non_decreasing(number):
    print(f"Цифры числа {number} справа налево упорядочены по неубыванию.")
else:
    print(f"Цифры числа {number} справа налево не упорядочены по неубыванию.")
