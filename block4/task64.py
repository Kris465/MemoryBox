number = int(input("Введите шестизначное число: "))


def is_happy_number(number):
    num_str = str(number)
    if len(num_str) != 6:
        return False

    first_half_sum = sum(int(num_str[i]) for i in range(3))
    second_half_sum = sum(int(num_str[i]) for i in range(3, 6))
    return first_half_sum == second_half_sum


if is_happy_number(number):
    print("Число счасливое")
else:
    print("Число не счастливое")
