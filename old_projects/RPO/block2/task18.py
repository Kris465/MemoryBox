def get_three_digit_number():

    while True:
        try:
            number = int(input("Введите трёхзначное число: "))
            if 99 < number < 1000:
                return number
            else:
                print("Введённое число должно быть трёхзначным!")
        except ValueError:
            print("Вы ввели некорректное значение. Попробуйте ещё раз.")


def rearrange_digits(number):

    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10
    return hundreds, tens, units


def generate_permutations(hundreds, tens, units):

    permutations = [
        (hundreds * 100 + tens * 10 + units),
        (hundreds * 100 + units * 10 + tens),
        (tens * 100 + hundreds * 10 + units),
        (tens * 100 + units * 10 + hundreds),
        (units * 100 + hundreds * 10 + tens),
        (units * 100 + tens * 10 + hundreds)
    ]
    return permutations


def display_results(permutations):

    for i, permutation in enumerate(permutations, start=1):
        print(f"Перестановка {i}: {permutation}")


if __name__ == "__main__":

    three_digit_number = get_three_digit_number()

    hundreds, tens, units = rearrange_digits(three_digit_number)

    permutations = generate_permutations(hundreds, tens, units)

    display_results(permutations)
