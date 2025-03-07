def is_digits_non_decreasing(n):
    # Преобразуем число в строку
    number_str = str(n)
    
    # Проверяем неубывание цифр
    for i in range(len(number_str) - 1):
        if number_str[i] > number_str[i + 1]:
            return False
    return True

# Примеры использования:
numbers_to_test = [1368, 1669, 1782]

for number in numbers_to_test:
    if is_digits_non_decreasing(number):
        print(f"{number} - последовательность цифр упорядочена по неубыванию")
    else:
        print(f"{number} - последовательность цифр не упорядочена по неубыванию")
