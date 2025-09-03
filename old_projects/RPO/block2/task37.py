def find_kth_digit(k):
    if k < 1 or k > 180:
        return "k должно быть в диапазоне от 1 до 180"

    pair_number = (k + 1) // 2
    two_digit_number = 10 + (pair_number - 1)
    if k % 2 == 0:
        kth_digit = two_digit_number % 10
    else:
        kth_digit = two_digit_number // 10
    return pair_number, two_digit_number, kth_digit


k = int(input("Введите число: "))
pair_number, two_digit_number, kth_digit = find_kth_digit(k)
print(f"а) Номер пары цифр: {pair_number}")
print(f"б) Двузначное число: {two_digit_number}")
print(f"в) {k}-я цифра: {kth_digit}")
