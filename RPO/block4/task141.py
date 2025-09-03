def is_sum_even(a, n):
    total_sum = 0

    for i in range(n):
        total_sum += a + i

    if total_sum % 2 == 0:
        return True
    else:
        return False


a = int(input("Введите начальный номер квартиры: "))
n = int(input("Введите количество квартир: "))
if is_sum_even(a, n):
    print("Сумма номеров всех квартир является чётной.")
else:
    print("Сумма номеров всех квартир является нечётной.")
