def find_kth_digit(k):

    if k < 1 or k > 150:
        return "k должно быть в диапазоне от 1 до 150"
    


    number_index = (k - 1) // 3
    three_digit_number = 101 + number_index
    

    position_in_number = (k - 1) % 3
    

    if position_in_number == 0:
        kth_digit = three_digit_number // 100
    elif position_in_number == 1:
        kth_digit = (three_digit_number // 10) % 10
    else:
        kth_digit = three_digit_number % 10
    
    return three_digit_number, position_in_number + 1, kth_digit


k = 7
number, position, digit = find_kth_digit(k)
print(f"k = {k}: Трехзначное число = {number}, Позиция в числе = {position}, Цифра = {digit}")
