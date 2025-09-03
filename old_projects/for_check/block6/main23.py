def analyze_number(n, a, z, x, y):
    # Преобразуем число в строку для удобной работы с цифрами
    digits = str(n)
    
    # а) Количество цифр a
    count_a = sum(1 for digit in digits if digit == str(a))
    
    # б) Количество цифр, кратных z
    count_multiple_z = sum(1 for digit in digits if int(digit) % z == 0)
    
    # в) Сумма цифр, больших a
    sum_greater_a = sum(int(digit) for digit in digits if int(digit) > a)
    
    # г) Количество цифр x и y
    count_x_y = sum(1 for digit in digits if digit in (str(x), str(y)))
    
    return {
        'количество_цифр_a': count_a,
        'количество_цифр_кратных_z': count_multiple_z,
        'сумма_цифр_больше_a': sum_greater_a,
        'количество_цифр_x_и_y': count_x_y
    }

# Пример использования
number = 123450
a = 3  # значение для сравнения
z = 2  # делитель для проверки кратности
x = 0  # первая искомая цифра
y = 5  # вторая искомая цифра

result = analyze_number(number, a, z, x, y)
print(f"Анализ числа {number}:")
for key, value in result.items():
    print(f"{key}: {value}")
