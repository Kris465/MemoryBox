def to_digit_array(number_str):
    """Преобразует строку в список цифр (в порядке записи числа)"""
    return list(map(int, number_str))


def add_big_numbers(num1_str, num2_str):
    a = list(map(int, reversed(num1_str)))
    b = list(map(int, reversed(num2_str)))

    max_len = max(len(a), len(b))
    result = []
    carry = 0

    for i in range(max_len):
        digit_a = a[i] if i < len(a) else 0
        digit_b = b[i] if i < len(b) else 0
        total = digit_a + digit_b + carry
        result.append(total % 10)
        carry = total // 10

    if carry > 0:
        result.append(carry)

    return ''.join(map(str, reversed(result)))


def subtract_big_numbers(num1_str, num2_str):
    def compare(num1, num2):
        if len(num1) != len(num2):
            return len(num1) > len(num2)
        for i in range(len(num1)):
            if num1[i] != num2[i]:
                return num1[i] > num2[i]
        return True  # числа равны

    if not compare(num1_str, num2_str):
        raise ValueError("Первое число должно быть больше или равно \
            второму для корректного вычитания.")

    a = list(map(int, reversed(num1_str)))
    b = list(map(int, reversed(num2_str)))

    result = []
    borrow = 0

    for i in range(len(a)):
        digit_a = a[i]
        digit_b = b[i] if i < len(b) else 0

        digit_a -= borrow
        borrow = 0

        if digit_a < digit_b:
            digit_a += 10
            borrow = 1

        result.append(digit_a - digit_b)

    # Удаляем лишние нули справа (в конце списка, так как он обратный)
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return ''.join(map(str, reversed(result)))
