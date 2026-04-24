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


def rearrange_digits(number):

    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    ones = number % 10
    return thousands, hundreds, tens, ones


def generate_permutations(digits):

    permutations = [
        (digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]),
        (digits[0] * 1000 + digits[3] * 100 + digits[2] * 10 + digits[1]),
        (digits[1] * 1000 + digits[0] * 100 + digits[3] * 10 + digits[2]),
        (digits[1] * 1000 + digits[2] * 100 + digits[0] * 10 + digits[3]),
        (digits[2] * 1000 + digits[1] * 100 + digits[0] * 10 + digits[3]),
        (digits[2] * 1000 + digits[3] * 100 + digits[1] * 10 + digits[0]),
        (digits[3] * 1000 + digits[0] * 100 + digits[1] * 10 + digits[2]),
        (digits[3] * 1000 + digits[2] * 100 + digits[0] * 10 + digits[1])
    ]
    return permutations


def display_results(permutations):

    for i, permutation in enumerate(permutations, start=1):
        print(f"Перестановка {i}: {permutation}")


if __name__ == "__main__":

    four_digit_number = get_four_digit_number()

    digits = rearrange_digits(four_digit_number)

    permutations = generate_permutations(digits)

    display_results(permutations)
