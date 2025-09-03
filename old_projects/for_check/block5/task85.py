def reverse_number(n):
    # Преобразуем число в строку и разворачиваем её
    reversed_str = str(n)[::-1]
    # Преобразуем обратно в целое число
    reversed_num = int(reversed_str)
    return reversed_num


number = input('Введите число: ')
reversed_number = reverse_number(number)
print(f"Исходное число: {number}, Перевернутое число: {reversed_number}")
