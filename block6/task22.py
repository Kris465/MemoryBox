def analyze_number(n):
    str_n = str(n)
    

    count_3 = str_n.count('3')
    

    last_digit = str_n[-1]
    count_last_digit = str_n.count(last_digit)
    

    count_even = sum(1 for digit in str_n if int(digit) % 2 == 0)
    

    sum_greater_than_5 = sum(int(digit) for digit in str_n if int(digit) > 5)
    

    product_greater_than_7 = 1
    has_greater_than_7 = False
    for digit in str_n:
        if int(digit) > 7:
            product_greater_than_7 *= int(digit)
            has_greater_than_7 = True
    if not has_greater_than_7:
        product_greater_than_7 = 0
    

    count_0_and_5 = str_n.count('0') + str_n.count('5')
    
    # Вывод результатов
    print(f"Количество цифр 3: {count_3}")
    print(f"Количество раз, когда встречается последняя цифра ({last_digit}): {count_last_digit}")
    print(f"Количество четных цифр: {count_even}")
    print(f"Сумма цифр, больших 5: {sum_greater_than_5}")
    print(f"Произведение цифр, больших 7: {product_greater_than_7}")
    print(f"Количество цифр 0 и 5: {count_0_and_5}")


number = int(input("Введите натуральное число: "))
analyze_number(number)