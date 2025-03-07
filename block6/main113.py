def sum_of_last_m_digits(n, m):
    # Преобразуем число в строку и берем последние m цифр
    last_digits = str(n)[-m:]
    
    # Преобразуем последние цифры в числа и суммируем их
    return sum(int(digit) for digit in last_digits)

# Пример использования
number = 123456
m = 3
result = sum_of_last_m_digits(number, m)
print(f"Сумма последних {m} цифр числа {number} равна {result}")
