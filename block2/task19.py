def get_four_digit_number():

    while True:
        try:
            number = int(input("Введите четырёхзначное число: "))
            if 999 < number < 10000:
                return number
            else:
                print("Введённое число должно быть четырёхзначным!")
        except ValueError:
            print("Вы ввели некорректное значение. Попробуйте ещё раз.")

def calculate_sum_and_product(number):

    one_num = number % 10
    two_num = (number // 10) % 10
    three_num = (number // 100) % 10
    four_num = (number // 1000) % 10
    sum_num = one_num + two_num + three_num + four_num
    proizv_num = one_num * two_num * three_num * four_num
    return sum_num, proizv_num

if __name__ == "__main__":

    four_digit_number = get_four_digit_number()
    

    sum_result, product_result = calculate_sum_and_product(four_digit_number)
    
    # Выводим результаты
    print(f"Сумма четырёхзначного числа: {sum_result}")
    print(f"Произведение четырёхзначного числа: {product_result}")
