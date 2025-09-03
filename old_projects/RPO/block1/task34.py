def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Ошибка! Введено некорректное значение. Попробуйте снова.")


a = get_number("Введите число a: ")
b = get_number("Введите число b: ")

if a == 0:
    print("Ошибка: a не может быть равен нулю.")
else:
    x = -b / a
    print(f"Результат: x = {x}")
