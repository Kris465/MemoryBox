def analyze_number(num):
    # Преобразуем число в строку для работы с цифрами
    num_str = str(num)
    
    # Извлекаем цифры
    digits = [int(d) for d in num_str]
    
    # а) Сумма его цифр больше 10?
    sum_of_digits = sum(digits)
    print("Сумма цифр больше 10: ", sum_of_digits > 10)
    
    # б) Произведение его цифр меньше 50?
    product_of_digits = 1
    for d in digits:
        product_of_digits *= d
    print("Произведение цифр меньше 50: ", product_of_digits < 50)
    
    # в) Количество его цифр является четным числом?
    num_of_digits = len(digits)
    print("Количество цифр четное: ", num_of_digits % 2 == 0)
    
    # г) Это число четырехзначное?
    print("Число четырехзначное: ", 1000 <= num < 10000)
    
    # д) Первая цифра не превышает 6?
    first_digit = digits[0]
    print("Первая цифра не превышает 6: ", first_digit <= 6)
    
    # е) Оно начинается и заканчивается одной и той же цифрой?
    print("Начинается и заканчивается одной и той же цифрой: ", digits[0] == digits[-1])
    
    # ж) Какая из его цифр больше: первая или последняя?
    last_digit = digits[-1]
    if first_digit > last_digit:
        print("Первая цифра больше последней")
    elif first_digit < last_digit:
        print("Последняя цифра больше первой")
    else:
        print("Первая и последняя цифры равны")

# Пример использования
num = int(input("Введите натуральное число: "))
analyze_number(num)
