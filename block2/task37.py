def find_digit_info(k):
    numbers = ''.join(str(i) for i in range(10, 100))
    if not (1 <= k <= len(numbers)):
        return "k находится вне допустимого диапазона."
    pair_index = (k - 1) // 2 + 1  
    digit_position_within_pair = (k - 1) % 2 + 1  
    pair_start_index = (k - 1) // 2 * 2  
    two_digit_number = numbers[pair_start_index:pair_start_index + 2]
    k_digit = numbers[k - 1]
    return {
        'номер пары': pair_index,
        'двузначное число': two_digit_number,
        'k-я цифра': k_digit,
        'четность': 'четная' if k % 2 == 0 else 'нечетная'
    }
k = 10

result = find_digit_info(k)
print(result)
