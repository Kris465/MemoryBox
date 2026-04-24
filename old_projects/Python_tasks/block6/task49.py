def check_digits(n):

    n_str = str(n)

    has_three = '3' in n_str

    has_two_and_five = '2' in n_str and '5' in n_str

    return has_three, has_two_and_five


number = int(input("Введите натуральное число: "))
has_three, has_two_and_five = check_digits(number)

print(f"Цифра 3 {'есть' if has_three else 'отсутствует'} в числе.")
print(f"Цифры 2 и 5 {'есть' if has_two_and_five else 'отсутствуют'} в числе.")
