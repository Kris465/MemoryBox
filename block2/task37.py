def find_digit_position(k):

    pair_number = (k // 2) + 1

    number = (k // 2) + 10

    if k % 2 == 0:

        digit = number % 10
    else:

        digit = number // 10

    return pair_number, number, digit


k = int(input("Введите значение k: "))
pair_number, number, digit = find_digit_position(k)
print(f"Номер пары цифр: {pair_number}")
print(f"Двузначное число: {number}")
print(f"k-я цифра: {digit}")
